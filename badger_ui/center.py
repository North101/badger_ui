from badger_ui.util import Offset, Size

from .base import App, Widget


class Center(Widget):
  def __init__(
      self,
      child: Widget,
  ):
    self.child = child
  
  def measure(self, app: 'App', size: Size) -> Size:
    return self.child.measure(app, size)

  def render(self, app: App, size: Size, offset: Offset):
    center_x = size.width // 2
    center_y = size.height // 2
    child_size = self.child.measure(app, size)
    self.child.render(
      app=app,
      size=child_size,
      offset=offset + Offset(center_x - (child_size.width // 2), center_y - (child_size.height // 2)),
    )
