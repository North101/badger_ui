import badger2040w
from collections import namedtuple

Size = namedtuple('Size', [
    'width',
    'height',
])


class Offset:
  x: int
  y: int

  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  def __add__(self, other: 'Offset'):
    return Offset(self.x + other.x, self.y + other.y)

  def __sub__(self, other: 'Offset'):
    return Offset(self.x - other.x, self.y - other.y)

  def __repr__(self):
    return f'Offset(x={self.x}, y={self.y})'


class Image:
  def __init__(self, path: str, width: int, height: int):
    self.path = path
    self.width = width
    self.height = height
    self.data = bytearray(width * height // 8)
  
  def load(self):
    with open(self.path, 'r') as f:
      f.readinto(self.data)
  
  def draw(self, display: badger2040w.Badger2040W, offset: Offset):
    display.image(
      self.data,
      w=self.width,
      h=self.height,
      x=offset.x,
      y=offset.y,
    )


class IconSheet:
  def __init__(self, path: str, size: int, count: int):
    self.path = path
    self.size = size
    self.count = count
    self.data = bytearray(int(self.sheet_width * self.size / 8))

  @property
  def sheet_width(self):
    return self.size * self.count

  def load(self):
    with open(self.path, 'r') as f:
      f.readinto(self.data)

  def icon(self, display: badger2040w.Badger2040W, icon_index: int, offset: Offset):
    display.set_pen(0)
    display.icon(
        self.data,
        icon_index,
        self.sheet_width,
        self.size,
        offset.x,
        offset.y,
    )
  