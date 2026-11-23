"""Example inputs for HW1 -- "Spider-Man: Swing Through the City".

Coordinates are (row, column), with (0, 0) the top-left tile.
The graders will run check.py with their own (possibly larger) inputs.
"""

# -----------------------------------------------------------------------------
# Non-competitive problems
# -----------------------------------------------------------------------------
non_comp_problems = [
    # 1. Warm-up: open 3x3 block, short web shooters.
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "heights": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 10, "max_web_fluid": 10,
                      "swing_range": 1, "villain_damage": 3},
        "villains": {},
        "web_caches": [],
    },
    # 2. Same block, almost out of web fluid -> no solution.
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "heights": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 3, "max_web_fluid": 10,
                      "swing_range": 1, "villain_damage": 3},
        "villains": {},
        "web_caches": [],
    },
    # 3. Long swings: range 3 on an open 5x5 block.
    {
        "map": [
            ['P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'D'],
        ],
        "heights": [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 20, "max_web_fluid": 20,
                      "swing_range": 3, "villain_damage": 3},
        "villains": {},
        "web_caches": [],
    },
    # 4. Skyscrapers block long swings -- the direct line is not always available.
    {
        "map": [
            ['P', 'P', 'P', 'P', 'P'],
            ['I', 'I', 'I', 'I', 'P'],
            ['P', 'P', 'P', 'P', 'P'],
            ['P', 'I', 'I', 'I', 'I'],
            ['P', 'P', 'P', 'P', 'D'],
        ],
        "heights": [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 30, "max_web_fluid": 30,
                      "swing_range": 4, "villain_damage": 3},
        "villains": {},
        "web_caches": [],
    },
    # 5. The Vulture is perched in the middle of the block.
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "heights": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 10, "max_web_fluid": 10,
                      "swing_range": 1, "villain_damage": 10},
        "villains": {"Vulture": [(1, 1)]},
        "web_caches": [],
    },
    # 6. Rooftops of different heights: climbing costs web fluid, dropping is free.
    {
        "map": [
            ['P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'D'],
        ],
        "heights": [
            [0, 0, 0, 4],
            [0, 2, 2, 4],
            [0, 2, 2, 4],
            [1, 1, 1, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 7, "max_web_fluid": 10,
                      "swing_range": 3, "villain_damage": 3},
        "villains": {},
        "web_caches": [],
    },
    # 7. Empty web shooters -- refill first.
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'P', 'P'],
            ['P', 'P', 'D'],
        ],
        "heights": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 0, "max_web_fluid": 10,
                      "swing_range": 2, "villain_damage": 3},
        "villains": {},
        "web_caches": [{"location": (0, 0), "refill_amount": 7, "cooldown": 1}],
    },
    # 8. A small cache with a cooldown: refill, wait, refill again.
    {
        "map": [
            ['P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'D'],
        ],
        "heights": [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 0, "max_web_fluid": 10,
                      "swing_range": 3, "villain_damage": 3},
        "villains": {},
        "web_caches": [{"location": (0, 0), "refill_amount": 3, "cooldown": 2}],
    },
    # 9. Doctor Octopus patrols the only gap in the wall -- timing matters.
    {
        "map": [
            ['P', 'P', 'P', 'P', 'P'],
            ['I', 'I', 'P', 'I', 'I'],
            ['P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'D'],
        ],
        "heights": [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 9, "max_web_fluid": 12,
                      "swing_range": 2, "villain_damage": 8},
        "villains": {"Doc Ock": [(0, 2), (1, 2), (2, 2), (2, 3)]},
        "web_caches": [],
    },
    # 10. Two caches, a capped tank, and a wall (cache on the far side).
    {
        "map": [
            ['P', 'P', 'P'],
            ['P', 'I', 'I'],
            ['P', 'I', 'D'],
            ['P', 'P', 'P'],
        ],
        "heights": [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 0, "max_web_fluid": 3,
                      "swing_range": 2, "villain_damage": 10},
        "villains": {},
        "web_caches": [{"location": (0, 0), "refill_amount": 3, "cooldown": 1},
                       {"location": (3, 0), "refill_amount": 3, "cooldown": 1}],
    },
    # 11. Queens rooftops: two villains, two caches, rooftop heights.
    {
        "map": [
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'D', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'P'],
        ],
        "heights": [
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 2, 2],
            [1, 1, 0, 0, 3, 3],
            [2, 2, 1, 1, 3, 3],
            [2, 2, 1, 1, 0, 2],
            [2, 2, 2, 2, 2, 2],
        ],
        "spiderman": {"starting_location": (1, 1), "starting_web_fluid": 3, "max_web_fluid": 21,
                      "swing_range": 2, "villain_damage": 10},
        "villains": {"Green Goblin": [(2, 1), (1, 1), (1, 2), (2, 2)],
                     "Rhino": [(3, 2), (3, 3), (3, 4)]},
        "web_caches": [{"location": (0, 0), "refill_amount": 3, "cooldown": 1},
                       {"location": (0, 3), "refill_amount": 10, "cooldown": 3}],
    },
    # 12. Midtown: walls, three villains, two caches, rooftop heights.
    {
        "map": [
            ['P', 'P', 'P', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'I', 'I', 'P'],
            ['P', 'P', 'P', 'I', 'P', 'I'],
            ['P', 'P', 'I', 'P', 'P', 'P'],
            ['P', 'P', 'P', 'P', 'P', 'I'],
            ['I', 'I', 'P', 'P', 'D', 'I'],
            ['P', 'P', 'P', 'I', 'P', 'P'],
        ],
        "heights": [
            [0, 0, 1, 1, 2, 2],
            [0, 0, 1, 0, 0, 2],
            [0, 0, 1, 0, 3, 0],
            [1, 1, 0, 2, 3, 3],
            [1, 1, 0, 2, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 1, 1],
        ],
        "spiderman": {"starting_location": (1, 1), "starting_web_fluid": 3, "max_web_fluid": 21,
                      "swing_range": 3, "villain_damage": 10},
        "villains": {"Green Goblin": [(2, 1), (1, 1), (1, 2), (2, 2)],
                     "Rhino": [(3, 3), (3, 4), (3, 5)],
                     "Mysterio": [(2, 4)]},
        "web_caches": [{"location": (0, 0), "refill_amount": 3, "cooldown": 1},
                       {"location": (0, 3), "refill_amount": 10, "cooldown": 3}],
    },
]


# -----------------------------------------------------------------------------
# Example competitive problems (larger). Graders will use their own.
# -----------------------------------------------------------------------------
def _row_patrol(r, c0, c1):
    return [(r, c) for c in range(c0, c1 + 1)]


def _col_patrol(c, r0, r1):
    return [(r, c) for r in range(r0, r1 + 1)]


comp_problems = [
    # C1. 25x25 Hell's Kitchen grid of buildings.
    {
        "map": [["D" if (i, j) == (24, 24) else
                 "I" if (i % 6 in (2, 3) and j % 6 in (2, 3)) else "P"
                 for j in range(25)] for i in range(25)],
        "heights": [[((i // 6) + (j // 6)) % 4 for j in range(25)] for i in range(25)],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 20, "max_web_fluid": 40,
                      "swing_range": 4, "villain_damage": 6},
        "villains": {"Kingpin": _row_patrol(5, 0, 24),
                     "Bullseye": _col_patrol(17, 0, 24)},
        "web_caches": [{"location": (12, 0), "refill_amount": 25, "cooldown": 3},
                       {"location": (18, 12), "refill_amount": 25, "cooldown": 3}],
    },
    # C2. 30x30 with a river (row of buildings) crossed by three bridges.
    {
        "map": [["D" if (i, j) == (29, 29) else
                 "I" if (i == 14 and j not in (3, 15, 26)) else "P"
                 for j in range(30)] for i in range(30)],
        "heights": [[2 * ((i // 10 + j // 10) % 3) for j in range(30)] for i in range(30)],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 25, "max_web_fluid": 45,
                      "swing_range": 5, "villain_damage": 8},
        "villains": {"Scorpion": _col_patrol(15, 10, 18),
                     "Shocker": _row_patrol(20, 5, 28),
                     "Electro": _col_patrol(26, 12, 16)},
        "web_caches": [{"location": (8, 8), "refill_amount": 30, "cooldown": 4},
                       {"location": (22, 22), "refill_amount": 30, "cooldown": 4}],
    },
    # C3. 40x40 four districts separated by building walls with small gaps.
    {
        "map": [["D" if (i, j) == (39, 39) else
                 "I" if ((i == 20 and j not in (5, 34)) or (j == 20 and i not in (10, 30))) else "P"
                 for j in range(40)] for i in range(40)],
        "heights": [[3 if (i < 20) != (j < 20) else (i // 10) % 2 for j in range(40)] for i in range(40)],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 30, "max_web_fluid": 60,
                      "swing_range": 6, "villain_damage": 10},
        "villains": {"Venom": _col_patrol(5, 15, 25),
                     "Carnage": _row_patrol(30, 15, 25),
                     "Lizard": _col_patrol(34, 15, 25)},
        "web_caches": [{"location": (10, 10), "refill_amount": 40, "cooldown": 4},
                       {"location": (30, 30), "refill_amount": 40, "cooldown": 4},
                       {"location": (10, 30), "refill_amount": 20, "cooldown": 2}],
    },
    # C4. 50x50 Manhattan: tight web fluid, four patrolling villains, four caches.
    {
        "map": [["D" if (i, j) == (49, 49) else
                 "I" if ((10 <= i <= 12 and 10 <= j <= 40) or (30 <= i <= 35 and 8 <= j <= 30)
                         or (20 <= i <= 25 and 35 <= j <= 49)
                         or (j == 25 and (13 <= i <= 29 or i >= 36) and i != 45)) else "P"
                 for j in range(50)] for i in range(50)],
        "heights": [[(i // 25) * 2 + (j // 25) for j in range(50)] for i in range(50)],
        "spiderman": {"starting_location": (0, 0), "starting_web_fluid": 30, "max_web_fluid": 60,
                      "swing_range": 4, "villain_damage": 8},
        "villains": {"Venom": _col_patrol(5, 0, 9),
                     "Carnage": _row_patrol(45, 20, 29),
                     "Sandman": _col_patrol(44, 0, 9),
                     "Mysterio": _row_patrol(15, 0, 11)},
        "web_caches": [{"location": (5, 5), "refill_amount": 30, "cooldown": 5},
                       {"location": (16, 30), "refill_amount": 30, "cooldown": 5},
                       {"location": (40, 40), "refill_amount": 30, "cooldown": 5},
                       {"location": (45, 10), "refill_amount": 15, "cooldown": 3}],
    },
]

