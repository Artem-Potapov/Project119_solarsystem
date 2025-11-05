import turtle as trtl
from potapov_collections import BetterTurtle
import time


class Planet:
  def __init__(self, _turtle: BetterTurtle, _orbit: int, _orbit_speed: int, _main_color: str, _dawn_color: str|None = None):
    self.turtle = _turtle
    self.orbit_radius = _orbit
    self.main_color = _main_color
    self.dawn_color = _dawn_color
    self.orbit_speed = _orbit_speed
  
  def orbit(self, speed: int|None=None, steps: int=3):
    if speed is not None:
      spd = speed
    else:
      spd = self.orbit_speed
    self.turtle.circle(self.orbit_radius, extent=spd, steps=steps)
    time.sleep(0.01)

#init sun
sun = BetterTurtle(shape="circle")
sun.color("yellow")
sun.turtlesize(7)

colors = ["brown", "#EE00EE", "green", "orange"]
sizes = [2, 3, 4, 3]
orbit_speeds = [3, 5, 7, 10]

planets = []
for col, size, pos, spd in zip(colors, sizes, range(1, 5), orbit_speeds):
  planet_turtle = BetterTurtle(start_pos=(pos*100+40, 0), shape="circle")
  planet_turtle.speed(0)
  planet_turtle.color(col)
  planet_turtle.turtlesize(size)
  planet_turtle.setheading(90)
  planet = Planet(planet_turtle, pos*100+40, spd, col)
  planets.append(planet)

while True:
  for planet in planets:
    planet.orbit()

app = trtl.Screen()
app.mainloop()