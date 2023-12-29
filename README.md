### Note to (debugging) developers, especially PyQt developers using `QSlider` sigals
#### See `Player_and_slider.py` for full code. 

When you try to put together the relationships of sliders and players, it is possible to call each other (make both of
them interdependent), like this:

```python
self.slider.sliderMoved.connect(self.set_pos)
self.slider.sliderPressed.connect(self.set_pos_smooth)
self.player.durationChanged.connect(self.update_dur)
self.player.positionChanged.connect(self.update_pos)  
```

And the corresponding (simplified) script goes like this:

```python
def set_pos(self, pos):
    self.player.setPosition(pos)


def set_pos_smooth(self):
    self.player.setPosition(self.slider.value())


def update_pos(self, pos):
    self.slider.setValue(pos)


def update_dur(self, dur):
    self.slider.setRange(0, dur)                               
```

However, it is important to know that **different slider signals varies, and have differnet influences on performace.**

- `sliderMoved`->`set_pos`: Detects the movement of the slider, only triggered by changing playback position of player (
  user's intentions does not work, as the slider bounces back). Passes the current position to script (`pos`).
- `valueChanged`: Detects the movement of the slider, triggered both by user and player. Passes the current position to
  script.
  <br>**Caution: this makes audio stuck and pop, even when played without user interfering, and might be regarded as
  buffer issue (which confused me for a while), but the actual cause is unsure.**`
- `sliderPressed`->`set_pos_smooth`: An intermediate solution to fix the `valueChanged` issue. Only trigged by users,
  but does **not** pass the current position to script, a little tweak in the script `set_pos_smooth` is made.

In my code, only `sliderMoved` and `sliderPressed` are used, to avoid the issue above. The control of the slider between
player and user is separate. 