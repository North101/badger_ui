from badger_ui.util import Offset, Size

from .base import App, Widget


class Column(Widget):
  def __init__(self, children: list[Widget]) -> None:
    super().__init__()

    self.children = children

  def __call__(self, app: App, size: Size, offset: Offset):
    for child in self.children:
      child_size = child.measure(app, size)
      child(app, child_size, offset)
      offset += Offset(0, child_size.height)
