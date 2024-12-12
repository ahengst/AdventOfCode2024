# Day 02b

# Algorithm / Python topics used today
#   create a useful function to use in various situations
#   copying a list with [:] helped avoid changes to the original list
#   using pop to remove an element from a list

# learned...
#   lookup "shallow copy" and "deep copy" in Python
#   For AoC, open and save two empty text files for today's puzzle input.

#

import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

# DIGITS = "0123456789"

FNAME = "Day02testa.txt"
FNAME = "Day02a.txt"

safecount = 0


def is_safe(numbers) -> bool:
    safe = True
    increasing = False
    decreasing = False

    prev = numbers[0]

    for number in numbers[1:]:
        diff = int(number) - int(prev)
        if abs(diff) > 3:
            safe = False
        if diff == 0:
            safe = False
        if diff > 0:
            increasing = True
        elif diff < 0:
            decreasing = True

        prev = number

    if increasing and decreasing:
        logging.debug(f"unsafe increasing and decreasing")
        safe = False
    logging.debug(f"END func call")
    return safe


# read file into a list of integer lists
infile = open(FNAME)  # opens file for (default=read)
for line in infile:
    logging.debug(f"line {line}")
    safeinoneway = False
    numbers = line.split()
    for i in range(len(numbers)):
        # construct list where numbers is missing the ith element
        testrange = numbers[:]

        testrange.pop(i)
        if is_safe(testrange):
            safeinoneway = True
            logging.debug(f"safeinoneway {safeinoneway} range {testrange}")

    if is_safe(numbers):
        safeinoneway = True
        logging.debug(f"safeinoneway {safeinoneway} whole set")

    if safeinoneway:
        logging.debug(f"safeinoneway {safeinoneway} numbers {numbers}")
        safecount += 1

logging.info(f"{safecount} safe rows found")


print(f"{safecount} safe rows")
