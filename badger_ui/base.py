import badger2040

from badger_ui.buttons import ButtonHandler
from badger_ui.util import Offset, Size


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
      display: badger2040.Badger2040,
      size=Size(width=badger2040.WIDTH, height=badger2040.HEIGHT),
      clear_color: int = 15,
      offset: Offset = None,
  ):
    self.display = display
    self.size = size
    self.offset = offset or Offset(0, 0)
    self.child: Widget = None
    self.buttons = ButtonHandler()
    self.clear_color = clear_color
    self.dirty = True

  def on_button(self, app: 'App', pressed: dict[int, bool]) -> bool:
    return self.child.on_button(app, pressed)

  def test_button(self) -> bool:
    if not self.buttons.dirty:
      return

    pressed = self.buttons.pressed()
    self.buttons.dirty = self.buttons.any()

    result = self.on_button(self, pressed)
    self.dirty = self.dirty or result

    return result

  def clear(self):
    self.display.pen(self.clear_color)
    self.display.clear()

  def update(self):
    self.test_button()
    if not self.dirty:
      if not self.buttons.dirty:
        self.display.update()
        self.display.halt()
      return

    self.clear()
    self.render(self, self.size, self.offset)
    self.display.update()
    self.dirty = False

  def render(self, app: 'App', size: Size, offset: Offset):
    self.child.render(app, size, offset)
