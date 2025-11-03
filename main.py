import turtle as trtl
from potapov_collections import BetterTurtle

turtle = BetterTurtle()
app = trtl.Screen()

turtle.speed(0)

for i in range(360):
  turtle.circle(100, 1, 1)
turtle.tiltangle()

app.mainloop()