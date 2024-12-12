# Day 03a

# for part B look only for don't()...do() areas,
#    I used NotePad++ to separate lines at don't and do, removed all the don't lines...
#    It may be best to pre-parse the puzzle input using Sed/awk

# Algorithm / Python topics used today
#   regex to find 1-3 digits, then a comma, then 1-3 digits:
#   regex   mul\([0-9]{1,3},[0-9]{1,3}\)

# learned...
#   parse long strings??

#


import logging
import re

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

FNAME = "Day03b.txt"
FNAME = "Day03b2.txt"
FNAME = "Day03testa.txt"

REGX1 = "mul\\([0-9]{1,3},[0-9]{1,3}\\)"

sumofproducts = 0
mulenabled = True


def multy(instruc) -> int:
    # extract the two numbers from the pattern, multiply them, and return the result
    # split the string at the comma
    # remove the "mul(" from the first number
    # remove the ")" from the second number
    # multiply the two numbers
    # return the result
    instruc = instruc.split(",")
    instruc[0] = instruc[0][4:]
    instruc[1] = instruc[1][:-1]
    logging.debug(instruc)
    return int(instruc[0]) * int(instruc[1])
    # return 1


# find all copies of REGX1 in file FNAME
with open(FNAME) as f:
    for line in f:
        logging.debug("start of line")
        # logging.debug(line)
        # find all matches of REGX1 in line
        matches = re.findall(REGX1, line)
        logging.debug(matches)
        for match in matches:
            if mulenabled:
                sumofproducts += multy(match)


logging.debug(f"{sumofproducts} and other info")

print(f"Sum of products {sumofproducts}")
