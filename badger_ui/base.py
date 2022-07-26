import gc

import badger2040

from badger_ui.buttons import ButtonHandler
from badger_ui.util import Offset, Size

display = badger2040.Badger2040()


class Widget:
  def measure(self, app: 'App', size: Size) -> Size:
    return size

  def on_button(self, app: 'App', pressed: dict[int, bool]) -> bool:
    return False

  def render(self, app: 'App', size: Size, offset: Offset):
    pass


class App(Widget):
  def __init__(
      self,
      update_speed=badger2040.UPDATE_TURBO,
      size=Size(width=badger2040.WIDTH, height=badger2040.HEIGHT),
      clear_color: int = 15,
      offset: Offset | None = None,
  ):
    self.display = display
    self.display.update_speed(update_speed)
    self.size = size
    self.offset = offset or Offset(0, 0)
    self.child: Widget | None = None
    self.buttons = ButtonHandler()
    self.clear_color = clear_color
    self.dirty = True

  def on_button(self, app: 'App', pressed: dict[int, bool]) -> bool:
    if not self.child:
      return False
    return self.child.on_button(app, pressed)

  def test_button(self):
    if not self.buttons.dirty:
      return

    pressed = self.buttons.pressed()
    self.buttons.dirty = self.buttons.any()

    self.dirty = self.on_button(self, pressed) or self.dirty

  def clear(self):
    self.display.pen(self.clear_color)
    self.display.clear()

  def update(self):
    self.test_button()
    if not self.dirty:
      if not self.buttons.dirty:
        self.display.update()
        gc.collect()
        self.display.halt()
      return

    self.clear()
    self.render(self, self.size, self.offset)
    self.display.update()
    self.dirty = False

  def render(self, app: 'App', size: Size, offset: Offset):
    from badger_ui.text import text

    if self.child:
      self.child.render(app, size, offset)

    used = gc.mem_alloc()
    free = gc.mem_free()
    total = used + free
    text(
        app=app,
        size=size,
        offset=Offset(0, self.size.height - 10),
        text=f'{int(used / total * 100)}%',
        line_height=12,
        thickness=2,
        scale=0.4,
    )

  def run(self):
    while True:
      self.update()
