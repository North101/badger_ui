import gc

from badger_ui.buttons import ButtonHandler
from badger_ui.util import Offset, Size

import badger2040

display = badger2040.Badger2040()


class Widget:
  def init(self):
    pass

  def measure(self, app: 'App', size: Size) -> Size:
    return size

  def on_button(self, app: 'App', pressed: dict[int, bool]) -> bool:
    return False

  def render(self, app: 'App', size: Size, offset: Offset):
    pass


class App(Widget):
  def __init__(
      self,
      update_speed=badger2040.UPDATE_FAST,
      size=Size(width=badger2040.WIDTH, height=badger2040.HEIGHT),
      clear_color: int = 15,
      offset: Offset | None = None,
  ):
    self.display = display
    self.display.set_update_speed(update_speed)
    self.size = size
    self.offset = offset or Offset(0, 0)
    self._child: Widget | None = None
    self.buttons = ButtonHandler()
    self.clear_color = clear_color
    self.dirty = True

  def close(self):
    pass

  @property
  def child(self):
    return self._child

  @child.setter
  def child(self, value):
    if self._child is value:
      return

    self._child = value
    self._child.init()

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
    self.display.set_pen(self.clear_color)
    self.display.clear()

  def update(self):
    self.test_button()
    if not self.dirty:
      # if not self.buttons.dirty:
      #  self.display.update()
      #  gc.collect()
      #  self.display.halt()
      return

    self.clear()
    self.render(self, self.size, self.offset)
    self.display.update()
    self.dirty = False
    gc.collect()

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


class AppRunner:
  def __init__(self):
    self._app: App | None = None

  @property
  def app(self):
    return self._app

  @app.setter
  def app(self, value: App):
    if self._app is value:
      return
    elif self._app is not None:
      self._app.close()

    self._app = value
    self._app.init()
    self.update()

  def update(self):
    if self.app:
      self.app.update()


app_runner = AppRunner()
