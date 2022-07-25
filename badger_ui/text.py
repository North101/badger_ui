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
    app.display.font(self.font)
    app.display.pen(self.color)
    app.display.thickness(self.thickness)
    app.display.text(
      self.text,
      offset.x,
      offset.y,
      scale=self.scale,
    )

