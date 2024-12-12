# Day 04a

# across 221  XMAS
# across 235  backwards SAMX


# Algorithm / Python topics used today
#   traversed 2D array in SIX distinct loops, 4 of them diagonals
#   Better way to do diagonals(??) is (like in Part B), to step through all the 4x4 BOXES

# learned...
#   use .strip() to remove trailing newline, for cleaner text arrays
#   thing2
#


import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")


FNAME = "Day04a.txt"
ACROSS = 140
DOWN = 140
FNAME = "Day04atest.txt"
ACROSS = 10
DOWN = 10

WORD = 4

XMASright = 0
SAMXright = 0
XMASdown = 0
SAMXdown = 0
XMASur = 0
SAMXur = 0
XMASdr = 0
SAMXdr = 0


def tally(rrooww):
    # count the number of XMAS and SAMX in the string
    # return the counts
    logging.debug(f"   tallying {rrooww}")
    return rrooww.count("XMAS") + rrooww.count("SAMX")


# test every row
# read Day04.txt as LINES
logging.debug("Looking at lines")
with open(FNAME) as f:
    for line in f:
        # find all matches of both words in line
        n = tally(line)
        XMASright += n
        logging.debug(f"line has {n} matches")

logging.info(f"{XMASright} XMASright")

logging.debug("Looking at columns")
# test every column
# make empty list of columns
CCOLS = []
for i in range(ACROSS):
    CCOLS.append("")
# Read file into a list of strings

with open(FNAME) as f:
    for line in f:
        for i in range(ACROSS):
            ch = line[i]
            CCOLS[i] += ch
for col in CCOLS:
    n = tally(col)
    XMASdown += n
    logging.debug(f"column has {n} matches")

logging.info(f"{XMASdown} XMASdown")

logging.debug("Looking at diag-downs top half")
# starting at top left, slice diag-downs moving to the right (long to short)
for c in range(ACROSS):
    diag = ""
    for r in range(ACROSS - c):
        diag += CCOLS[c + r][r]
    n = tally(diag)
    XMASdr += n
    logging.debug(f"diag has {n} matches")

logging.debug("Looking at diag-downs bottom half")
# starting at top left, slice diag-downs moving down (long to short)
for r in range(ACROSS - 1):
    diag = ""
    for c in range(ACROSS - r - 1):
        diag += CCOLS[c][r + c + 1]
    n = tally(diag)
    XMASdr += n
    logging.debug(f"diag has {n} matches")

logging.info(f"{XMASdr} XMASdr")

logging.debug("Looking at diag-ups top half")
# starting at top left, slice diag-ups moving down (short to long)
for r in range(ACROSS):
    diag = ""
    for c in range(r + 1):
        diag += CCOLS[c][r - c]
    n = tally(diag)
    XMASur += n
    logging.debug(f"diag has {n} matches")

logging.debug("Looking at diag-ups bottom half")
# starting at bottom left, slice diag-ups moving down (long to short)
for c in range(ACROSS - 1):
    diag = ""
    for r in range(ACROSS - c - 1):
        diag += CCOLS[c + r + 1][ACROSS - r - 1]
    n = tally(diag)
    XMASur += n
    logging.debug(f"diag has {n} matches")

logging.info(f"{XMASur} XMASur")

nn = XMASright + XMASdown + XMASdr + XMASur
print(f"combined total {nn}")
