# Day 08b

# Algorithm / Python topics used today
#    use regex to...

# learned...
#   a function could return nothing, just modify the list passed to it
#   can enumerate any iterator:      for rr, rrow in enumerate(roof[:r]):
#

# Copilot came up with these on its own:
#   anti[rwalk] = anti[rwalk][:cwalk] + "#" + anti[rwalk][cwalk + 1 :]


import logging
import copy

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

FNAME = "Day08atest.txt"
FNAME = "Day08a.txt"


roof = []
with open(FNAME) as f:
    for line in f:
        roof.append(line.strip())
width = len(roof[0])
height = len(roof)
anti = copy.deepcopy(roof)


def resonanceline(ar, ac, arr, acc, anti: list):
    # calculate -all- antinodes (line of nodes) absolute positions
    # if posision is in the array, mark spot(s) with "#"
    rdelta = arr - ar
    cdelta = acc - ac
    logging.debug(f"resonances for {ar} ac {ac} arr {arr} acc {acc}")

    # walk the line of nodes starting at one node.
    rwalk = ar
    cwalk = ac
    # walk backward until off grid
    while rwalk >= 0 and cwalk >= 0 and rwalk < height and cwalk < width:
        anti[rwalk] = anti[rwalk][:cwalk] + "#" + anti[rwalk][cwalk + 1 :]
        rwalk -= rdelta
        cwalk -= cdelta

    # walk the line of nodes starting at one node.
    rwalk = ar
    cwalk = ac
    # walk forward until off grid
    while rwalk < height and cwalk < width and rwalk >= 0 and cwalk >= 0:
        anti[rwalk] = anti[rwalk][:cwalk] + "#" + anti[rwalk][cwalk + 1 :]
        rwalk += rdelta
        cwalk += cdelta

    return


# scan the roof, first looking for the *second* antenna, then all possible *first* antennas
for r, row in enumerate(roof):
    for c, col in enumerate(row):
        if col != ".":
            # look for all pairs where the other node is "above" or "same row" as this one
            #  (above works better for indexes)
            for rr, rrow in enumerate(roof[:r]):
                for cc, ccol in enumerate(rrow):
                    if cc == c and rr == r:
                        # skip the THIS node node
                        continue
                    if ccol == col:
                        # found a pair at coords: (r, c) and (rr, cc) above
                        # First antinode is at (r )
                        logging.debug(f"checking {r}, {c} and {rr}, {cc}")
                        resonanceline(r, c, rr, cc, anti)
            logging.debug(f"antinode at {r}, {c}")


# count the number of "#" in anti[]
antinodes = 0
for row in anti:
    antinodes += row.count("#")

logging.info(f"{antinodes}")


print(antinodes)
