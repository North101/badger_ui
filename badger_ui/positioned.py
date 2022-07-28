from badger_ui.util import Offset, Size

from .base import App, Widget

class Positioned(Widget):
  def __init__(self, child: Widget, offset: Offset) -> None:
    super().__init__()

    self.child = child
    self.offset = offset
  
  def __call__(self, app: 'App', size: Size, offset: Offset):
    return self.child(app, size, offset + self.offset)