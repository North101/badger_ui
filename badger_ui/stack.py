from badger_ui.util import Offset, Size

from .base import App, Widget


class Stack(Widget):
  def __init__(self, children: list[Widget]) -> None:
    super().__init__()

    self.children = children

  def __call__(self, app: 'App', size: Size, offset: Offset):
    for child in self.children:
      child(app, size, offset)
