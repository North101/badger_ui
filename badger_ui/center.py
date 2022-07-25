from badger_ui.util import Offset, Size

from .base import App, Widget


class Center(Widget):
  def __init__(
      self,
      child: Widget,
  ):
    self.child = child

  def render(self, app: App, size: Size, offset: Offset):
    center_x = size.width // 2
    center_y = size.height // 2
    self.child.render(
      app=app,
      size=size,
      offset=offset + Offset(center_x - (self.child.measure(app, size).width // 2), center_y),
    )
