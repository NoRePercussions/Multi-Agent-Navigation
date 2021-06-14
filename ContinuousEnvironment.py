# Environment for agents
# thshea 2021


from Agent import Agent
from Location import Location
from Environment import Environment

from math import floor


class ContinuousEnvironment(Environment):
    continuous = True

    """
    Creates an environment with coordinate space
    [0, rows) x [0, cols)
    """
    def __init__(self, x: int, y: int,
                 rows:int =10, cols:int =10):
        self.size = (x, y)
        self.gridsize = (rows, cols)
        # Empty rXc grid
        self.grid = [ [[]]*cols ]*rows  # type: list[list[list[Agent]]]
        self.agents = []  # type: list[Agent]

    def addAgent(self, agent: Agent, loc: Location=None):
        self.agents += [agent]
        if loc is None:
            self._putAgentInGrid(agent)
        else:
            self._putAgentInGrid(agent, loc)

    def _putAgentInGrid(self, agent: Agent, loc: Location=None):
        if loc is None:
            loc = agent.loc
        rcenter = floor(loc.x / (self.size[0] / self.gridsize[0]))
        ccenter = floor(loc.y / (self.size[1] / self.gridsize[1]))

        self.grid[rcenter][ccenter] += [agent]

    def _removeAgentFromGrid(self, agent: Agent):
        loc = agent.loc
        rcenter = floor(loc.x / (self.size[0] / self.gridsize[0]))
        ccenter = floor(loc.y / (self.size[1] / self.gridsize[1]))

        self.grid[rcenter][ccenter].remove(agent)

    def iterate(self):
        for agent in self.agents:
            agent.iterate()

    def getAgentsInRadius(self, loc:Location, rad:int):
        rcenter = loc.x // (self.size[0] / self.gridsize[0])
        ccenter = loc.y // (self.size[1] / self.gridsize[1])
        rdelta  = rad // self.gridsize[0]  + 1
        cdelta  = rad // self.gridsize[1]  + 1

        nearbyAgents = []

        for roffset in range(-rdelta, rdelta+1):
            if not 0 <= rcenter+roffset < self.gridsize[0]:
                continue
            for coffset in range(-cdelta, cdelta+1):
                if not 0 <= ccenter + coffset < self.gridsize[1]:
                    continue
                for agent in self.grid[int(rcenter+roffset)] \
                                      [int(ccenter+coffset)]:
                    if loc.distanceTo(agent.loc) < rad:
                        nearbyAgents += [agent]

        return nearbyAgents
