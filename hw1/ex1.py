import search
import random
import math
import itertools


ids = ["111111111", "111111111"]


class SpiderManProblem(search.Problem):
    """This class implements the Spider-Man web-swinging problem according to the
    problem description file."""

    def __init__(self, initial):
        """`initial` is the input dictionary described in the assignment.
        Convert it to YOUR hashable state representation before calling the
        parent constructor, and store any static information (map, villain
        paths, caches, ...) on self."""
        search.Problem.__init__(self, initial)

    def actions(self, state):
        """Return the valid actions that can be executed in the given state."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given action in the given state."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal state."""
        raise NotImplementedError

    def h(self, node):
        """
        Heuristic function for A* search.
        Estimates the minimum number of turns needed to reach the goal.
        """
        raise NotImplementedError


def create_spiderman_problem(game):
    return SpiderManProblem(game)


def astar_search(problem, heuristic):
    """Return the goal node if found, None otherwise."""
    raise NotImplementedError
