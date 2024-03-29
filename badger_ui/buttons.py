import time

from machine import Pin

import badger2040


class ButtonCallback:
  def __call__(self, pin: int):
    pass


class Button:
  def __init__(self, pin: Pin, invert=False, repeat_time=200, hold_time=1000):
    self.pin = pin
    self.invert = invert
    self.repeat_time = repeat_time
    self.hold_time = hold_time
    self.last_state = False
    self.pressed = False
    self.pressed_time = 0

  def read(self):
    current_time = time.ticks_ms()
    state = self.raw()
    changed = state != self.last_state
    self.last_state = state

    if changed:
      if state:
        self.pressed_time = current_time
        self.pressed = True
        self.last_time = current_time
        return True
      else:
        self.pressed_time = 0
        self.pressed = False
        self.last_time = 0

    if self.repeat_time == 0:
      return False

    if self.pressed:
      repeat_rate = self.repeat_time
      if self.hold_time > 0 and current_time - self.pressed_time > self.hold_time:
        repeat_rate /= 3
      if current_time - self.last_time > repeat_rate:
        self.last_time = current_time
        return True

    return False

  def raw(self):
    if self.invert:
      return not self.pin.value()
    else:
      return self.pin.value()

  @property
  def is_pressed(self):
    return self.raw()


class ButtonHandler:
  buttons = {
      button: Button(pin)
      for button, pin in badger2040.BUTTONS.items()
  }

  def __init__(self):
    self.dirty = False
    self._pressed = {}
    for button in self.buttons.values():
      button.pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self.handler)

  def handler(self, pin: int):
    self.dirty = True

  def any(self):
    return any((
        True
        for button in self.buttons.values()
        if button.is_pressed
    ))

  def pressed(self):
    for pin, button in self.buttons.items():
      self._pressed[pin] = button.read()
    return self._pressed

  def __getitem__(self, pin: int):
    return self.buttons[pin]
