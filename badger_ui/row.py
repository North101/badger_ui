from badger_ui.util import Offset, Size

from .base import App, Widget


class Row(Widget):
  def __init__(self, children: list[Widget]) -> None:
    super().__init__()

    self.children = children

  def measure(self, app: 'App', size: Size) -> Size:
    width = 0
    height = 0
    for child in self.children:
      child_size = child.measure(app, size)
      height = max(height, child_size.height)
      width += child_size.width

    return Size(width, height)

  def render(self, app: App, size: Size, offset: Offset):
    for child in self.children:
      child_size = child.measure(app, size)
      child.render(app, child_size, offset)
      offset += Offset(child_size.width, 0)
