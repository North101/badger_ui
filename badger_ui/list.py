import badger2040

from badger_ui.util import Offset, Size

from .base import App, Widget
from .scrollbar import ScrollbarWidget


class ListItemBuilder:
  def __call__(self, index: int, selected: bool) -> Widget:
    pass


class ListWidget(Widget):
  _selected_index = 0
  children: list[Widget] = None

  def __init__(
      self,
      item_height: int,
      item_count: int,
      item_builder: ListItemBuilder,
      page_item_count: int,
      selected_index: int = 0,
  ):
    self.item_count = item_count
    self.item_height = item_height
    self.item_builder = item_builder
    self.selected_index = selected_index
    self.page_item_count = page_item_count
    self.scrollbar_width = 6

  @property
  def page_index(self):
    return self.selected_index // self.page_item_count

  @property
  def page_count(self):
    return ((self.item_count - 1) // self.page_item_count) + 1

  @property
  def page_start(self):
    return self.page_index * self.page_item_count

  @property
  def page_stop(self):
    return self.page_start + self.page_item_count

  @property
  def selected_child_index(self):
    return self.selected_index % self.page_item_count

  @property
  def selected_child(self):
    i = self.selected_child_index
    return self.item_builder(
        index=i,
        selected=(i == self.selected_index),
    )

  def on_button(self, app: App, pressed: dict[int, bool]):
    if pressed[badger2040.BUTTON_UP]:
      self.selected_index = (self.selected_index - 1) % self.item_count
      return True
    elif pressed[badger2040.BUTTON_DOWN]:
      self.selected_index = (self.selected_index + 1) % self.item_count
      return True

    return self.selected_child.on_button(app, pressed)

  def render(self, app: App, size: Size, offset: Offset):
    for i in range(self.page_start, min(self.page_stop, self.item_count)):
      self.item_builder(
          index=i,
          selected=(i == self.selected_index),
      ).render(
          app=app,
          size=Size(size.width - self.scrollbar_width, self.item_height),
          offset=Offset(0, self.item_height * (i % self.page_item_count)),
      )

    ScrollbarWidget(
        current=self.page_index,
        count=self.page_count,
    ).render(app, Size(self.scrollbar_width, size.height), Offset(size.width - self.scrollbar_width, 0))
