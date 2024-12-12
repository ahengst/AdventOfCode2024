# Day 08

# Algorithm / Python topics used today
#    use regex to...

# learned...
#   thing1
#   thing2
#


import logging
import copy

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

FNAME = "Day08a.txt"
FNAME = "Day08atest.txt"


roof = []
with open(FNAME) as f:
    for line in f:
        logging.debug(f"line: {line}")
        roof.append(line.strip())
width = len(roof[0])
height = len(roof)
anti = copy.deepcopy(roof)


def resonance(ar, ac, arr, acc, anti: list):
    # calculate both antinodes absolute positions
    # if posision is in the array, mark spot(s) with "#"
    n1r = ar - (arr - ar)
    n1c = ac - (acc - ac)
    n2r = arr + (arr - ar)
    n2c = acc + (acc - ac)
    logging.debug(f"resonance at n1r {n1r} n1c {n1c} n2r {n2r} n2c {n2c}")
    if n1r >= 0 and n1r < height and n1c >= 0 and n1c < width:
        anti[n1r] = anti[n1r][:n1c] + "#" + anti[n1r][n1c + 1 :]
    if n2r >= 0 and n2r < height and n2c >= 0 and n2c < width:
        anti[n2r] = anti[n2r][:n2c] + "#" + anti[n2r][n2c + 1 :]
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
                        resonance(r, c, rr, cc, anti)
            logging.debug(f"antinode at {r}, {c}")


# count the number of "#" in anti[]
antinodes = 0
for row in anti:
    antinodes += row.count("#")

logging.info(f"{antinodes}")


print(antinodes)
