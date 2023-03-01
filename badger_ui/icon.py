from badger_ui import App, Offset, Size, Widget
from badger_ui.util import IconSheet


class IconWidget(Widget):
  def __init__(self, icons: IconSheet, icon_index: int):
    self.icons = icons
    self.icon_index = icon_index

  def measure(self, app: 'App', size: Size) -> Size:
    return Size(self.icons.size, self.icons.size)

  def render(self, app: 'App', size: Size, offset: Offset):
    self.icons.icon(
        app.display,
        self.icon_index,
        offset,
    )
