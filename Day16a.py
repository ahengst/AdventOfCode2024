# Day 16

# Algorithm / Python topics used today
#    UNFINISHED - attempt to avoid too much recursion by simplifying the warehouse map.
#    UNFINISHED - attempt to find simple(DONE) and loopy(??) dead ends in the warehouse map.
# learned...
#   thing1
#   thing2
#

# Copilot came up with these on its own:
#   blablabla

import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")


FNAME = "Day16atest.txt"
FNAME = "Day16a.txt"

# Import the warehouse map
w = []  # warehouse
startlin, startcol = 0, 2  # once we find the @, we'll store it here permanently
with open(FNAME) as f:
    for line in f:
        if len(line) > 2:
            w.append(line.strip())
            # find S in line
            if "S" in line:
                startlin = len(w) - 1
                startcol = line.find("S")
                # replace S with .
                w[startlin] = w[startlin][:startcol] + "." + w[startlin][startcol + 1 :]
logging.info(f"startlin {startlin} startcol {startcol}")
logging.debug(f"warehouse {w}")

# traverse warehouse to close all simple dead ends - this only finds hallway dead ends
while True:
    deadends = 0
    for l, lin in enumerate(w):
        if l == 0 or l == len(w) - 1:
            continue
        for c, col in enumerate(lin):
            if c == 0 or c == len(lin) - 1:
                continue
            if col == "#" or col == "E":
                continue
            if l == startlin and c == startcol:
                continue
            surround = []
            for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # up, down, left, right
                surround.append(w[l + d[0]][c + d[1]])
            if surround.count("#") == 3 and surround.count(".") == 1:
                w[l] = w[l][:c] + "#" + w[l][c + 1 :]
                deadends += 1
    if deadends == 0:
        break

# traverse warehouse to find loops that are dead ends, like this:
"""
    ###.#
    #...#
    #.###       <<< pinch point
    #...#
    #.#.#
    #...#
    #.###       <<< pinch point
    #...#
    #.#.#
    #...#
    #####
 """
# Possible Strategies:
#    1.  open area surrounded by walls.
#        aka the # on either side of the pinch point form a loop, and E is not inside the loop.
#    2.  drop an elf onto one open spot, stop when multiple paths are available.
#         ... If any elf can map more "hallway", do it. (single row of dots, not #, not digits)
#         ... Where multiple paths exist, drop another elf on the new-digit path.
#         ... if only one path remains, we've found the pinch point.
#         Data structure: list of test-paths.
#              testp-active=1  (increase by 1 for each new elf)(reduce by 1 for each elf that reaches a dead end)
#              state: lin, col, open/paused/finished
#    3.  follow path in both directions, stopping at any fork. If both paths lead to the same fork, we found a loop.
#        Mark the loop with L and close the fork with #
"""
    ###.#
    #...#
    #.###       <<< pinch point
    #...#
    #.#.#
    #...#
    #1###       <<< pinch point
    #122#
    #1#2#
    #112#    <<< arbitrary start here at #.1.# and send two elves #1 and #2.
    #####        Stop any time a 'numeric dead end' is reached.
                 Stop if only 1 elf is left and seal the loop.
    
    We might never detect a pretzel loop like this:
    ################
    #...........#...
    #.###.#.###.#.##
    #.#...#.#...#..#
    #.............##
    ################

    ################    << starting at top left, send elves #1 and #2
    #11111......#...
    #2###.#.###.#.##
    #2#333#.#...#..#     << at 3... new rule: 2 should wait for 3 to catch up.
    #2222.........##            ...so 1 and 2 will wait... 3 went now 2 can resume, then 3 can resume..
    ################
    
    ################    << starting at top left, send elves #1 and #2
    #11111111111#...
    #2###3#4###1#.##
    #2#333#4#551#..#     << at 3... new rule: 2 should wait for 3 to catch up.
    #2222222222...##            ... 3 is done and 1 can resume.. 2 waits..
    ################       ...1 spawns 4... 4 is done... 2 resumes... 2 spawns 5, 5 ends.
                           ...1 is sealed off (dead end not of 1's making)
 """

logging.debug(f"warehouse...")
# use logging to show w as strings separated by newlines
logging.info(f"\n".join(w))


bestscore = 0


# recursively follow all paths, without backtracking.
# warehouse map has been reduced by blocking dead-ends, but explore() could handle that.
# [ should we call explore for each step or is that too much recursion?  Let's not do that. ]
def explore(testmap, lin, col, direction, score):
    # we just landed at a next step spot, check options.
    # assuming no wide-open areas.
    # Are we at the end?
    #     ... if bestscore = 0 or  bestscore > score, set bestscore = score and preserve this route!
    # Is score > bestscore?  If so, return 0
    # if more than one direction is possible, call explore for each direction:
    #     ...ahead (add 1 to score)  -- cheapest route first...
    #     ...left (add 1000 to score)
    #     ...right (add 1000 to score)
    #     ...back (do not try this)
    #     whichever option had the lowest nonzero score, return that score, preserve that route.
    pass


def fork(map, lin, col) -> bool:  # Strategy #3
    foundloop = False
    # if one, or more than two directions are possible, do nothing.
    # two directions are possible, walk along each path until a fork is reached.
    # if the fork is the same, we've found a loop.
    # mark the loop with L and close the fork with #

    # if we find a loop, return True
    return foundloop


logging.info(f"{bestscore}")
