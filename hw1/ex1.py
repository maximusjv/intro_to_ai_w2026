import math

import search
from utils import FIFOQueue

ids = ["345062228", "215983750"]


class StaticState:  # avoid copy and hash

    def __init__(self,
        max_web_fluid,
        swing_range,
        heights,
        city,
        web_caches,
        villain_damage,
        villains: dict[str, list]
    ):
        self.swing_range = swing_range
        self.heights = heights
        self.city = city
        self.max_web_fluid = max_web_fluid
        self.villain_damage = villain_damage
        self.web_caches: dict[tuple[int, int], dict[str, int]] = {
            tuple(cache["location"]): {
                "refill_amount": cache["refill_amount"],
                "cooldown": cache["cooldown"],
            }
            for cache in web_caches
        }
        self.villains_paths = [
            [tuple(back_and_forth) for back_and_forth in (path + path[-2:0:-1])]
            for path in villains.values()
        ]  # full back-and-forth cycles; names are not important
        self.villains_lcm = math.lcm(*(len(path) for path in self.villains_paths))
        self._villains_by_turn: dict[int, dict[tuple[int, int], int]] = {}

        self.rows = len(city)
        self.cols = len(city[0])

        ## PREPROCESS
        for row in range(self.rows):
            for col in range(self.cols):
                if self.city[row][col] == 'D':
                    self.dest = (row, col)
                    break
            else:
                continue
            break

        self.maze_distance = self.solve_maze_distance()  # O(n^2), admissible heuristic

    def villains_at(self, turn: int) -> dict[tuple[int, int], int]:
        """Return {location: villain_count} at `turn` (memoized lazily by turn % lcm)."""
        turn %= self.villains_lcm
        cached = self._villains_by_turn.get(turn)
        if cached is not None:
            return cached
        counts: dict[tuple[int, int], int] = {}
        for path in self.villains_paths:
            loc = path[turn % len(path)]
            counts[loc] = counts.get(loc, 0) + 1
        self._villains_by_turn[turn] = counts
        return counts

    def solve_maze_distance(self) -> list[list[int | None]]:
        """Return minimum swings to the destination with no range or resource limits."""
        maze_distance: list[list[int | None]] = [[None for _ in row] for row in self.city]
        dest_row, dest_col = self.dest
        maze_distance[dest_row][dest_col] = 0

        horizontal_scanned = [[False] * self.cols for _ in self.city]
        vertical_scanned = [[False] * self.cols for _ in self.city]
        segment_scans = (
            (horizontal_scanned, ((0, -1), (0, 1))),
            (vertical_scanned, ((-1, 0), (1, 0))),
        )

        q = FIFOQueue()
        q.append((dest_row, dest_col, 0))
        while len(q) > 0:
            row, col, distance = q.pop()
            for scanned, directions in segment_scans:
                if scanned[row][col]:
                    continue
                # Every tile in this segment is one swing from its first dequeued tile.
                scanned[row][col] = True
                for dr, dc in directions:
                    next_row, next_col = row, col
                    while True:
                        next_row += dr
                        next_col += dc
                        if not (0 <= next_row < self.rows and 0 <= next_col < self.cols):
                            break
                        if self.city[next_row][next_col] == "I":
                            break
                        scanned[next_row][next_col] = True
                        if maze_distance[next_row][next_col] is None:
                            maze_distance[next_row][next_col] = distance + 1
                            q.append((next_row, next_col, distance + 1))

        return maze_distance
#
#     def solve_max_swing(self):
#         max_swing  = [[[0, 0, 0, 0] for _ in row] for row in self.city] # (left, right, up, down)
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 back_row = self.rows - 1 - row
#                 back_col = self.cols - 1 - col
#                 if col != 0:
#                     max_swing[row][col][0] = (
#                         max_swing[row][col - 1][0] + 1 if self.city[row][col - 1] != 'I' else 0
#                     )
#                     max_swing[row][back_col][1] = (
#                         max_swing[row][back_col + 1][1] + 1 if self.city[row][back_col + 1] != 'I' else 0
#                     )
#                 if row != 0:
#                     max_swing[row][col][2] = (
#                         max_swing[row - 1][col][2] + 1 if self.city[row - 1][col] != 'I' else 0
#                     )
#                     max_swing[back_row][col][3] = (
#                         max_swing[back_row + 1][col][3] + 1 if self.city[back_row + 1][col] != 'I' else 0
#                     )
#         return max_swing


class State:

    def __init__(self,
        global_state: StaticState,
        turn: int,
        location: tuple[int, int],
        web_fluid,
        web_cache_active_cooldowns: tuple[tuple[tuple, int]] | tuple,
        # cooldown left ((location, turns left, I use tuple for hashing and assume not many active,
        # but might be a bottleneck
        finished: bool,  # to make sure that ("finish",) was an action
    ):
        self.global_state = global_state
        self.turn = turn % self.global_state.villains_lcm
        self.location = tuple(location)
        self.web_fluid = web_fluid
        self.web_cache_active_cooldowns = web_cache_active_cooldowns
        self.finished = finished

    def villains_locations(self) -> dict[tuple[int, int], int]:
        return self.global_state.villains_at(self.turn)

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return (
            self.turn == other.turn and
            self.location == other.location and
            self.web_fluid == other.web_fluid and
            self.web_cache_active_cooldowns == other.web_cache_active_cooldowns and
            self.finished == other.finished
        )

    def __hash__(self):
        return hash((
            self.turn,
            self.location,
            self.web_fluid,
            self.web_cache_active_cooldowns,
            self.finished,
        ))


class SpiderManProblem(search.Problem):
    """This class implements the Spider-Man web-swinging problem according to the
    problem description file."""

    def __init__(self, initial):
        """`initial` is the input dictionary described in the assignment.
        Convert it to YOUR hashable state representation before calling the
        parent constructor, and store any static information (map, villain
        paths, caches, ...) on self."""
        spiderman = initial["spiderman"]
        self.static_state = StaticState(
            max_web_fluid=spiderman["max_web_fluid"],
            swing_range=spiderman["swing_range"],
            heights=initial["heights"],
            city=initial["map"],
            web_caches=initial["web_caches"],
            villain_damage=spiderman["villain_damage"],
            villains=initial["villains"],
        )
        initial_state = State(
            global_state=self.static_state,
            turn=0,
            location=tuple(spiderman["starting_location"]),
            web_fluid=spiderman["starting_web_fluid"],
            web_cache_active_cooldowns=(),
            finished=False,
        )
        search.Problem.__init__(self, initial_state)

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
