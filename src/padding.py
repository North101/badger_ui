from badger_ui import App, Offset, Size, Widget


class EdgeOffsets:
  def __init__(self, left: int = 0, top: int = 0, right: int = 0, bottom: int = 0):
    self.left = left
    self.top = top
    self.right = right
    self.bottom = bottom

  @classmethod
  def all(cls, value: int):
    return cls(
        left=value,
        top=value,
        right=value,
        bottom=value,
    )

  @classmethod
  def symetric(cls, horizontal: int = 0, vertical: int = 0):
    return cls(
        left=horizontal,
        top=vertical,
        right=horizontal,
        bottom=vertical,
    )


class Padding(Widget):
  def __init__(self, child: Widget, padding: EdgeOffsets):
    self.child = child
    self.padding = padding

  def measure(self, app: App, size: Size):
    child_size = self.child.measure(app, size)
    return Size(
        width=child_size.width + self.padding.left + self.padding.right,
        height=child_size.height + self.padding.top + self.padding.bottom,
    )

  def render(self, app: 'App', size: Size, offset: Offset):
    self.child.render(
        app,
        self.child.measure(app, size),
        offset + Offset(self.padding.left, self.padding.top),
    )
