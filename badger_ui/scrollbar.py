from badger_ui.util import Offset, Size

from .base import App, Widget


class ScrollbarWidget(Widget):
  def __init__(self, current=0, count=0):
    self.current = current
    self.count = count

  def render(self, app: App, size: Size, offset: Offset):
    if self.count == 1:
      return

    height = size.height

    # draw box
    start_x = offset.x
    start_y = offset.y
    stop_x = offset.x + size.width - 1
    stop_y = offset.y + height
    app.display.pen(0)
    # top
    app.display.line(
        start_x,
        start_y,
        stop_x,
        start_y,
    )
    # left
    app.display.line(
        start_x,
        start_y,
        start_x,
        stop_y,
    )
    app.display.line(
        start_x,
        stop_y,
        stop_x,
        stop_y,
    )
    app.display.line(
        stop_x,
        start_y,
        stop_x,
        stop_y,
    )

    # draw segment
    segment_height = height // self.count
    segment_y_offset = segment_height * self.current
    app.display.rectangle(
        offset.x,
        offset.y + segment_y_offset,
        size.width,
        segment_height,
    )
