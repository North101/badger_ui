from badger_ui.util import Offset, Size

from .base import App, Widget


class Center(Widget):
  def __init__(
      self,
      child: Widget,
  ):
    self.child = child

  def measure(self, app: 'App', size: Size) -> Size:
    return self.child.measure(app, size)

  def render(self, app: App, size: Size, offset: Offset):
    child_size = self.child.measure(app, size)
    self.child.render(
        app=app,
        size=child_size,
        offset=offset + Offset((size.width - child_size.width) // 2, (size.height - child_size.height) // 2),
    )


class Left(Widget):
  def __init__(
      self,
      child: Widget,
  ):
    self.child = child

  def measure(self, app: 'App', size: Size) -> Size:
    return self.child.measure(app, size)

  def render(self, app: App, size: Size, offset: Offset):
    child_size = self.child.measure(app, size)
    self.child.render(
        app=app,
        size=Size(child_size.width, size.height),
        offset=offset,
    )


class Right(Widget):
  def __init__(
      self,
      child: Widget,
  ):
    self.child = child

  def measure(self, app: 'App', size: Size) -> Size:
    return self.child.measure(app, size)

  def render(self, app: App, size: Size, offset: Offset):
    child_size = self.child.measure(app, size)
    self.child.render(
        app=app,
        size=Size(child_size.width, size.height),
        offset=offset + Offset(size.width - child_size.width, 0),
    )


class Top(Widget):
  def __init__(
      self,
      child: Widget,
  ):
    self.child = child

  def measure(self, app: 'App', size: Size) -> Size:
    return self.child.measure(app, size)

  def render(self, app: App, size: Size, offset: Offset):
    child_size = self.child.measure(app, size)
    self.child.render(
        app=app,
        size=Size(size.width, child_size.height),
        offset=offset,
    )


class Bottom(Widget):
  def __init__(
      self,
      child: Widget,
  ):
    self.child = child

  def measure(self, app: 'App', size: Size) -> Size:
    return self.child.measure(app, size)

  def render(self, app: App, size: Size, offset: Offset):
    child_size = self.child.measure(app, size)
    self.child.render(
        app=app,
        size=Size(size.width, child_size.height),
        offset=offset + Offset(0, size.height - child_size.height),
    )
