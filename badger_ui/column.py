from badger_ui.util import Offset, Size

from .base import App, Widget


class Column(Widget):
  def __init__(self, children: list[Widget]) -> None:
    super().__init__()

    self.children = children
  
  def measure(self, app: 'App', size: Size) -> Size:
    width = 0
    height = 0
    for child in self.children:
      child_size = child.measure(app, size)
      width = max(width, child_size.width)
      height += child_size.height
    
    return Size(width, height)

  def render(self, app: App, size: Size, offset: Offset):
    center_x = size.width // 2
    for child in self.children:
      child_size = child.measure(app, size)
      child.render(app, child_size, offset + Offset(center_x - (child_size.width // 2), 0))
      offset += Offset(0, child_size.height)
