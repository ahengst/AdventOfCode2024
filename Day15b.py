# Day 15b so far only just got cloned from 15a

# Algorithm / Python topics used today
#    decide whether to edit the input file (search & replace) or to slice and zip odd/even chars in each input line
#    new different logic for up&down (recursive) and left&right (straight line)

# learned...
#   thing1
#   thing2
#

# Copilot came up with these on its own:
#   blablabla

import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
# logging.critical / .error / .warning / .info / .debug(f"..")

BOXES = "O"
DIRECT = "<^>v"
DIRDICT = {"<": [0, -1], "^": [-1, 0], ">": [0, 1], "v": [1, 0]}  # row, col

FNAMEw = "Day15ats1.txt"
FNAME = "Day15ats2.txt"
FNAMEw = "Day15atest1.txt"
FNAME = "Day15atest2.txt"
FNAMEw = "Day15a1.txt"
FNAME = "Day15a2.txt"


def step(warehouse, poslin, poscol, direction):
    # based on look-ahead assessment, determine action
    #    if <any number of boxes> + space,
    # horizon string is everything straight ahead up to the wall

    #    if space, move forward
    if warehouse[poslin + DIRDICT[direction][0]][poscol + DIRDICT[direction][1]] == ".":
        return poslin + DIRDICT[direction][0], poscol + DIRDICT[direction][1]

    # #    if wall, do nothing   REDUNDANT, while loop catches this
    # if warehouse[poslin+DIRDICT[direction][0]][poscol+DIRDICT[direction][1]] == "#":
    #     return poslin, poscol

    #    if <one or more boxes> + wall, do nothing
    horizon = ""  # string of boxes, but has no use in this function..yet
    l, c = poslin, poscol
    while True:
        l += DIRDICT[direction][0]
        c += DIRDICT[direction][1]
        if warehouse[l][c] in BOXES:
            horizon += warehouse[l][c]
        elif warehouse[l][c] == "#":
            break
        elif warehouse[l][c] == ".":
            warehouse[l] = warehouse[l][:c] + "O" + warehouse[l][c + 1 :]
            poslin += DIRDICT[direction][0]
            poscol += DIRDICT[direction][1]
            warehouse[poslin] = (
                warehouse[poslin][:poscol] + "." + warehouse[poslin][poscol + 1 :]
            )
            break
        else:
            logging.error(f"unexpected character {warehouse[l][c]}")
    return poslin, poscol


w = []  # warehouse
startlin, startcol = 0, 0  # once we find the @, we'll store it here permanently
with open(FNAMEw) as f:
    for line in f:
        if len(line) > 2:
            w.append(line.strip())
            # find @ in line
            if "@" in line:
                startlin = len(w) - 1
                startcol = line.find("@")
                # replace @ with .
                w[startlin] = w[startlin][:startcol] + "." + w[startlin][startcol + 1 :]
logging.info(f"startlin {startlin} startcol {startcol}")

posl, posc = startlin, startcol  # current position while traversing the warehouse
for i, c in enumerate(open(FNAME).read().strip()):
    if c in DIRECT:
        posl, posc = step(w, posl, posc, c)


GPSsum = 0
for l, line in enumerate(w):
    for i, c in enumerate(line):
        if c in BOXES:
            GPSsum += (100 * l) + i

logging.info(f"{GPSsum} is the sum of the GPS coordinates of the boxes")
