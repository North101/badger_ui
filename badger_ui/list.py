import badger2040

from badger_ui.util import Offset, Size

from .base import App, Widget
from .scrollbar import scrollbar


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
    self.create_items()

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

  def create_items(self):
    self.items = [
        self.item_builder(
            index=i,
            selected=(i == self.selected_index),
        )
        for i in range(self.page_start, min(self.page_stop, self.item_count))
    ]

  def update_items(self, previous_page_index, previous_selected_index):
    if previous_page_index != self.page_index:
      return self.create_items()

    self.items[previous_selected_index - self.page_start] = self.item_builder(
        index=previous_selected_index,
        selected=False,
    )
    self.items[self.selected_child_index - self.page_start] = self.item_builder(
        index=self.selected_child_index,
        selected=True,
    )

  def on_button(self, app: App, pressed: dict[int, bool]):
    if pressed[badger2040.BUTTON_UP]:
      page_index = self.page_index
      selected_index = self.selected_index
      self.selected_index = (selected_index - 1) % self.item_count
      self.update_items(page_index, selected_index)
      return True

    elif pressed[badger2040.BUTTON_DOWN]:
      page_index = self.page_index
      selected_index = self.selected_index
      self.selected_index = (selected_index + 1) % self.item_count
      self.update_items(page_index, selected_index)
      return True

    return self.items[self.selected_child_index].on_button(app, pressed)

  def render(self, app: App, size: Size, offset: Offset):
    for i, item in enumerate(self.items, start=self.page_start):
      item.render(
          app=app,
          size=Size(size.width - self.scrollbar_width, self.item_height),
          offset=Offset(0, self.item_height * (i % self.page_item_count)),
      )

    scrollbar(
        app=app,
        size=Size(self.scrollbar_width, size.height),
        offset=Offset(size.width - self.scrollbar_width, 0),
        current=self.page_index,
        count=self.page_count,
    )
