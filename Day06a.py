# Day 06

# Algorithm / Python topics used today
#    use regex to...
#  in front: turn right
#  clear: go forward, leaving X behind

# learned...
#   thing1
#   thing2
#

# Copilot came up with these on its own:
#   blablabla

import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

FNAME = "Day06atest.txt"  # row 7 pos 6 [7,5]
WIDTH = 10
FNAME = "Day06a.txt"  # row 83 pos 36 [83,35]
WIDTH = 130

steps = 0
mapp = []
mapp.append(" " * (WIDTH + 2))
posrow = 0
poscol = 0
done = False

# direction table, 0 = up, 1 = right, 2 = down, 3 = left
# current direction is up (0)
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
currdir = 0

# import map array with space padding around edges
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

# replace "^" with "X" in mapp
# mapp[posrow] = mapp[posrow][:poscol] + str(currdir) + mapp[posrow][poscol + 1 :]
steps += 1

logging.info(f"posrow {posrow} poscol {poscol}")
print(f"positions as [row, col]: {posrow, poscol}")
print(f"char at that postion is {mapp[posrow][poscol]}")

while not done:
    mapprow = mapp[posrow]  # useful for debugging
    # look in 'direction' for next spot
    nextspot = mapp[posrow + direction[currdir][0]][poscol + direction[currdir][1]]

    # if not clear, turn right
    # if clear, move forward, if at edge we're done
    if nextspot == "#":
        currdir = (currdir + 1) % 4
        logging.debug(f"turning right.  new direction is {currdir}")
    elif nextspot == ".":
        # update position
        posrow += direction[currdir][0]
        poscol += direction[currdir][1]
        # put X in current position of mapp[]
        # Err list indices must be int or slices not tuple: mapp[posrow, poscol] = "X"
        logging.debug(f"oldrow {mapp[posrow]}")
        mapp[posrow] = mapp[posrow][:poscol] + str(currdir) + mapp[posrow][poscol + 1 :]
        logging.debug(f"xxxrow {mapp[posrow]}")
        steps += 1
    elif nextspot in "0123X^":
        # update position
        posrow += direction[currdir][0]
        poscol += direction[currdir][1]
        # we already have an X
    elif nextspot == " ":
        done = True
    else:
        logging.error(f"unexpected character {nextspot} at position {posrow, poscol}")


logging.info(f"{steps} steps")


print(steps)
