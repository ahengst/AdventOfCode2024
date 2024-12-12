# Day 03a

# for part B look only for don't()...do() areas,
#    I used NotePad++ to separate lines at don't and do, removed all the don't lines...

# Algorithm / Python topics used today
#    use regex to find "mul\({[0-9]}3, {[0-9]}3\)"
#   regex to find 1-3 digits, then a comma, then 1-3 digits
#   regex   mul\([0-9]{1,3},[0-9]{1,3}\)

# learned...
#   parse long strings

#   thing2
#


import logging
import re

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

DIGITS = "0123456789"

FNAME = "Day03testa.txt"
FNAME = "Day03b.txt"
FNAME = "Day03b2.txt"

REGX1 = "mul\\([0-9]{1,3},[0-9]{1,3}\\)"

sumofproducts = 0
mulenabled = 1


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
    return int(instruc[0]) * int(instruc[1]) * mulenabled
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
            sumofproducts += multy(match)


logging.debug(f"{sumofproducts} and other info")

print(sumofproducts)
print(f"175615763 minus sumofprod")
ans = 175615763 - sumofproducts
print(ans)
