# Test nav and avoidance
# thshea 2021

from Agent import Agent
from ContinuousEnvironment import ContinuousEnvironment
from Location import Location

env = ContinuousEnvironment(50, 50)

a = Agent()
a.putSelfInEnvironment(env, Location(2,2))
a.target = Location(48, 7)

b = Agent()
b.putSelfInEnvironment(env, Location(3,3))
b.target = Location(7, 48)

while a.loc.distanceTo(a.target) > .5:
    env.iterate()
    print(str(a.loc))
