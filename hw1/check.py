import ex1
import search
import time
from problems import non_comp_problems, comp_problems

_TIMEOUT = object()


def timeout_exec(func, args=(), kwargs={}, timeout_duration=10, default=None):
    """This function will spawn a thread and run the given function
    using the args, kwargs and return the given default value if the
    timeout_duration is exceeded.
    Note: Python cannot kill a thread. After a timeout the search keeps running
    in the background and slows down the next problems; restart check.py.
    """
    import threading

    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self, daemon=True)
            self.result = default

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except Exception as e:
                self.result = (-3, -3, e)

    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.is_alive():
        return default
    else:
        return it.result


def build_and_solve(game):
    """Builds the problem AND runs A*. Both count toward the time limit."""
    p = ex1.create_spiderman_problem(game)
    return ex1.astar_search(p, p.h)


def check_problem(game, timeout):
    """ Builds the problem with ex1.create_spiderman_problem and solves it with
    ex1.astar_search, within the given timeout (construction time included).
    Returns a tuple of (solution length, solution time, solution)

    (-1, -1, None)  means there was a timeout
    (-2, -2, None)  means the search finished and found no solution
    (-3, -3, ERR)   means there was some error ERR during search """

    t1 = time.time()
    s = timeout_exec(build_and_solve, args=[game], timeout_duration=timeout, default=_TIMEOUT)
    t2 = time.time()

    if isinstance(s, search.Node):
        solve = s
        solution = list(map(lambda n: n.action, solve.path()))[1:]
        return (len(solution), t2 - t1, solution)
    elif s is _TIMEOUT:
        return (-1, -1, None)
    elif s is None:
        return (-2, -2, None)
    else:
        return s


def format_warnings(solution):
    """Checks the FORMAT of a plan only. It does not check that the plan is legal."""
    warnings = []
    if not solution or solution[-1] != ("finish",):
        warnings.append('the plan does not end with ("finish",)')
    for a in solution:
        if not isinstance(a, tuple):
            warnings.append(f"action {a!r} is not a tuple")
            break
    return warnings


def solve_problems(problems):
    solved = 0
    for problem in problems:
        timeout = 60
        result = check_problem(problem, timeout)
        print("A* ", result)
        if result[2] is not None and result[0] != -3:
            solved = solved + 1
            for w in format_warnings(result[2]):
                print("    WARNING:", w)
    return solved


def main():
    print(ex1.ids)
    """Here goes the input you want to check"""

    solve_problems(non_comp_problems)
    # Uncomment to also run the larger example problems:
    # solve_problems(comp_problems)


if __name__ == '__main__':
    main()
