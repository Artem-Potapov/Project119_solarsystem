import turtle as trtl
from potapov_collections import BetterTurtle


sun = BetterTurtle(shape="circle")
sun.color("yellow")
sun.turtlesize(7)


app = trtl.Screen()
app.mainloop()