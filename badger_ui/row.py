from badger_ui.util import Offset, Size

from .base import App, Widget


class Row(Widget):
  def __init__(self, children: list[Widget]) -> None:
    super().__init__()

    self.children = children

  def render(self, app: App, size: Size, offset: Offset):
    for child in self.children:
      child_size = child.measure(app, size)
      child.render(app, child_size, offset)
      offset += Offset(child_size.width, 0)
