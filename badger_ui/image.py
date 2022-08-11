from badger_ui import App, Offset, Size, Widget
from badger_ui.util import Image


class ImageWidget(Widget):
  def __init__(self, image: Image):
    self.image = image

  def render(self, app: 'App', size: Size, offset: Offset):
    self.image.draw(app.display, offset)
