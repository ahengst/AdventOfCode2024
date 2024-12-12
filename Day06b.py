# Day 06

# Algorithm / Python topics used today
#    use regex to...
#  in front: turn right
#  clear: go forward, leaving X behind

# learned...
#   thing1
#   thing2
#


import logging
import copy  # needed for deepcopy

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

FNAME = "Day06a.txt"  # row 83 pos 36 [83,35]
WIDTH = 130
FNAME = "Day06atest.txt"  # row 7 pos 6 [7,5]
WIDTH = 10

# DIRECTION table, 0 = up, 1 = right, 2 = down, 3 = left
# current DIRECTION is up (0)
DIRECTION = [[-1, 0], [0, 1], [1, 0], [0, -1]]
steplimit = 10000  # we will reduce this later


def runmap(clean: list, startrow, startcol, obstaclerow: int, obstaclecol: int) -> int:
    onemapp = copy.deepcopy(clean)  # don't damage the original map
    steps = 0
    posrow = startrow
    poscol = startcol
    done = False

    currdir = 0

    if obstaclerow == 0 and obstaclecol == 0:
        pass
    else:
        # put # at obstruction
        onemapp[obstaclerow] = (
            onemapp[obstaclerow][:obstaclecol]
            + "#"
            + onemapp[obstaclerow][obstaclecol + 1 :]
        )

    # replace "^" with "X" in mapp
    # mapp[posrow] = mapp[posrow][:poscol] + str(currdir) + mapp[posrow][poscol + 1 :]
    steps += 1

    logging.info(f"posrow {posrow} poscol {poscol}")
    logging.info(f"positions as [row, col]: {posrow, poscol}")
    logging.info(f"char at that postion is {mapp[posrow][poscol]}")

    while not done and steps < steplimit:
        mapprow = onemapp[posrow]  # useful for debugging
        # look in 'direction' for next spot
        nextspot = onemapp[posrow + DIRECTION[currdir][0]][
            poscol + DIRECTION[currdir][1]
        ]

        # if not clear, turn right
        # if clear, move forward, if at edge we're done
        if nextspot == "#":
            currdir = (currdir + 1) % 4
            # logging.debug(f"turning right.  new direction is {currdir}")
        elif nextspot == ".":
            # update position
            posrow += DIRECTION[currdir][0]
            poscol += DIRECTION[currdir][1]
            # put X in current position of mapp[]
            # Err list indices must be int or slices not tuple: mapp[posrow, poscol] = "X"
            logging.debug(f"oldrow {onemapp[posrow]}")
            onemapp[posrow] = (
                onemapp[posrow][:poscol] + str(currdir) + onemapp[posrow][poscol + 1 :]
            )
            logging.debug(f"xxxrow {onemapp[posrow]}")
            steps += 1
        elif nextspot in "0123X^":
            # update position
            posrow += DIRECTION[currdir][0]
            poscol += DIRECTION[currdir][1]
            # we already have an X
        elif nextspot == " ":
            done = True
        else:
            logging.error(
                f"unexpected character {nextspot} at position {posrow, poscol}"
            )

    return steps, onemapp


mapp = []  # the original map.
Xmapp = []  # the map with Xs, or 0, 1, 2, 3, as we do later on.

# import map array with space padding around edges
mapp.append(" " * (WIDTH + 2))
with open(FNAME) as f:
    for line in f:
        logging.debug(f"line: {line}")
        mapprow = " " + line.strip() + " "
        # append row to mapp
        mapp.append(mapprow)
        if "^" in mapprow:
            posrow = len(mapp) - 1
            poscol = mapprow.find("^")

mapp.append(" " * (WIDTH + 2))

# do one run with no obstructions
steps, Xmapp = runmap(mapp, posrow, poscol, 0, 0)  # Hang on to the map with Xs
logging.info(f" FIRST CALL completed, Check variables now in debugger")
mapp = copy.deepcopy(Xmapp)  # and keep a master copy
steplimit = steps + 1000  # set a reasonable higher limit to detect infinite loops

# Traverse map, at every X (the only relevant place to put an obstruction), call runmap()
goodObstacles = 0
Xcount = 0
for row in range(1, len(mapp) - 1):
    for col in range(1, WIDTH - 1):
        if mapp[row][col] in "0123":
            Xcount += 1
            # runmap() with obstruction at row, col
            Xmapp = copy.deepcopy(mapp)  # make a copy we can ruin. &&& redundant
            steps, Xmapp = runmap(Xmapp, posrow, poscol, row, col)
            # the function returns 2 values, but we will discard Xmapp.
            logging.debug(f"steps {steps} obstruction at {row, col}")
            if steps > steplimit:
                goodObstacles += 1
logging.info(f"Xcount {Xcount} goodObstacles {goodObstacles}")

# # replace "^" with "X" in mapp
# # mapp[posrow] = mapp[posrow][:poscol] + str(currdir) + mapp[posrow][poscol + 1 :]
# steps += 1

# logging.info(f"posrow {posrow} poscol {poscol}")
# print(f"positions as [row, col]: {posrow, poscol}")
# print(f"char at that postion is {mapp[posrow][poscol]}")

# while not done:
#     mapprow = mapp[posrow]
#     # look in 'DIRECTION' for next spot
#     nextspot = mapp[posrow + DIRECTION[currdir][0]][poscol + DIRECTION[currdir][1]]

#     # if not clear, turn right
#     # if clear, move forward, if at edge we're done
#     if nextspot == "#":
#         currdir = (currdir + 1) % 4
#         logging.debug(f"turning right.  new DIRECTION is {currdir}")
#     elif nextspot == ".":
#         # update position
#         posrow += DIRECTION[currdir][0]
#         poscol += DIRECTION[currdir][1]
#         # put X in current position of mapp[]
#         # Err list indices must be int or slices not tuple: mapp[posrow, poscol] = "X"
#         logging.debug(f"oldrow {mapp[posrow]}")
#         mapp[posrow] = mapp[posrow][:poscol] + str(currdir) + mapp[posrow][poscol + 1 :]
#         logging.debug(f"xxxrow {mapp[posrow]}")
#         steps += 1
#     elif nextspot in "0123X^":
#         # update position
#         posrow += DIRECTION[currdir][0]
#         poscol += DIRECTION[currdir][1]
#         # we already have an X
#     elif nextspot == " ":
#         done = True
#     else:
#         logging.error(f"unexpected character {nextspot} at position {posrow, poscol}")


logging.info(f"{steps} steps")

# THIS IS A BAD ALGORITHM. IT ASSUMES APPROACH FROM DIRECTIONS THAT MAY NEVER HAVE HAPPENED.
# Traverse map, at every X (the only relevant place to put an obstruction)
#   test THOSE (max 4) possible loops where "X leads here"
#   Guard hits obstruction going in UP DIRECTION...
#     was there an X at ?  If not, skip
#     are we too close to (which) edge - skip
#     go clockwise to next # = down 1 and scan right
#     go clockwise to next # = scan down
#     go clockwise to next # = scan left
#     IF we hit a # AND guard is in line with the obstruction we have a loop.
#   Repeat for the 3 other DIRECTIONs


print(steps)
