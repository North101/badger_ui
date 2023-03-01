from badger_ui.util import Offset, Size

from .base import App, Widget


class SizedBox(Widget):
  def __init__(self, child: Widget, size: Size) -> None:
    self.child = child
    self.size = size

  def on_button(self, app: App, pressed: dict[int, bool]) -> bool:
    return self.child.on_button(app, pressed)
  
  def measure(self, app: App, size: Size) -> Size:
    return self.size
  
  def render(self, app: App, size: Size, offset: Offset):
    return self.child.render(app, self.size, offset)
