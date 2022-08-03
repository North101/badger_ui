from badger_ui.util import Offset, Size

from .base import App, Widget


class TextWidget(Widget):
  def __init__(
      self,
      text: str,
      line_height: int,
      font: str = 'sans',
      thickness: int = 1,
      color: int = 0,
      scale: float = 1,
  ):
    self.text = text
    self.font = font
    self.thickness = thickness
    self.color = color
    self.scale = scale
    self.line_height = line_height

  def measure(self, app: App, size: Size) -> Size:
    return Size(self.width(app), self.line_height)

  def width(self, app: App):
    return app.display.measure_text(self.text, scale=self.scale)

  def render(self, app: App, size: Size, offset: Offset):
    text(app, size, offset, self.text, self.line_height, self.font, self.thickness, self.color, self.scale)


def text(
    app: App,
    size: Size,
    offset: Offset,
    text: str,
    line_height,
    font: str = 'sans',
    thickness: int = 1,
    color: int = 0,
    scale: float = 1,
):
  app.display.font(font)
  app.display.pen(color)
  app.display.thickness(thickness)
  app.display.text(
      text,
      offset.x,
      offset.y + (line_height // 2),
      scale=scale,
  )
