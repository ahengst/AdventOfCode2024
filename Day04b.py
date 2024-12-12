# Day 04b

# Algorithm / Python topics used today
#    use regex to...

# learned...
#   thing1
#   thing2
#


import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")


FNAME = "Day04atest.txt"
ACROSS = 10
DOWN = 10
FNAME = "Day04a.txt"
ACROSS = 140
DOWN = 140

WORD = 4

Xmas = 0


# Read file into a list of strings
RROWS = []

with open(FNAME) as f:
    for line in f:
        RROWS.append(line.strip())


# For every 9x9 send 9 chars to regex test
# Starting at top left, row by row, to Last-2, Last-2

logging.debug("Looking at lines")

for c in range(ACROSS - 2):
    for r in range(ACROSS - 2):
        # Test the "x" as 6-chars topleft-bottomright + botleft-topright
        teststr = (
            RROWS[c][r]
            + RROWS[c + 1][r + 1]
            + RROWS[c + 2][r + 2]
            + RROWS[c][r + 2]
            + RROWS[c + 1][r + 1]
            + RROWS[c + 2][r]
        )
        if (
            teststr == "MASMAS"
            or teststr == "SAMMAS"
            or teststr == "MASSAM"
            or teststr == "SAMSAM"
        ):
            Xmas += 1


logging.info(f"{Xmas} Xmas")


print(f"combined total {Xmas}")
