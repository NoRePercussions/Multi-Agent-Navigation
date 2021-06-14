# Environment generic for type hints
# thshea 2021
import Agent
import Location


class Environment:
    size = None  # type: tuple[int, int]
    grid = None  # type: list[list[list[Agent]]]
    agents = None
    gridsize = None
    continuous = None

    def __init__(self, x, y, rows=None, cols=None):
        None

    def addAgent(self, agent: Agent, loc: Location=None) -> None:
        None

    def _putAgentInGrid(self, agent: Agent, loc: Location=None) -> None:
        None
        #todo rmag here

    def getAgentsInRadius(self, loc: Location, rad: int) -> int:
        return None
