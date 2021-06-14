# Navigation agent
# thshea 2021

from Environment import Environment
from Location import Location
from math import pi, tau


class Agent:
    def __init__(self):
        self.env = None     # type: Environment.Environment
        self.loc = None     # type: Location.Location
        self.target = None  # type: Location.Location


    def putSelfInEnvironment(self, env, loc=None):
        self.env = env
        self.loc = loc
        env.addAgent(self)


    def iterate(self):
        self.env._removeAgentFromGrid(self)
        self.loc = self.getMove()
        self.env._putAgentInGrid(self)


    def getMove(self):
        maxloc = self.loc.getLocationInDirection(0)
        maxval = self.score(maxloc)

        checks = 32 if self.env.continuous else 4

        for dir in range(1, checks):
            loc = self.loc.getLocationInDirection(tau * dir / checks)
            score = self.score(loc)

            if score < maxval:
                maxval = score
                maxloc = loc

        return maxloc


    def score(self, loc: Location):
        if(self.env.continuous):
            distalg = loc.distanceTo
        else:
            distalg = loc.taxicabDistanceTo

        score = distalg(self.target) if self.target is not None else 0

        agents = self.env.getAgentsInRadius(self.loc, 10)

        for agent in agents:
            score += 1/distalg(agent.loc)**2

        return score
