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
      underline=False,
  ):
    self.text = text
    self.font = font
    self.thickness = thickness
    self.color = color
    self.scale = scale
    self.line_height = line_height
    self.underline = underline

  def measure(self, app: App, size: Size) -> Size:
    return Size(self.width(app), self.line_height)

  def width(self, app: App):
    app.display.set_font(self.font)
    app.display.set_thickness(self.thickness)
    return app.display.measure_text(self.text, scale=self.scale)

  def render(self, app: App, size: Size, offset: Offset):
    text(
        app,
        size,
        offset,
        self.text,
        self.line_height,
        self.font,
        self.thickness,
        self.color,
        self.scale,
        self.underline)


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
    underline=False,
):
  app.display.set_font(font)
  app.display.set_pen(color)
  app.display.set_thickness(thickness)
  app.display.text(
      text,
      offset.x,
      offset.y + (line_height // 2),
      scale=scale,
  )
  if underline:
    app.display.line(
        offset.x,
        offset.y + line_height,
        offset.x + size.width,
        offset.y + line_height,
    )
