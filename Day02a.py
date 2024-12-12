# Day 02a
# learned...
#   thing1
#   thing2
#
# Algorithm ideas
#    read into a list of lists
#    Decide if list is ordered or

import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

# DIGITS = "0123456789"
safecount = 0

FNAME = "Day02testa.txt"
FNAME = "Day02a.txt"

# read file into a list of integer lists
infile = open(FNAME)  # opens file for (default=read)
for line in infile:
    logging.debug(f"line {line}")
    # split line by spaces into list of numbers
    safe = True
    increasing = False
    decreasing = False
    numbers = line.split()

    prev = int(numbers[0])

    for number in numbers[1:]:
        logging.debug(f"number {number}")
        diff = int(number) - prev
        if abs(diff) > 3:
            logging.debug(f"n unsafe 3")
            safe = False
        if diff == 0:
            logging.debug(f"n unsafe 0")
            safe = False
        if diff > 0:
            increasing = True
        elif diff < 0:
            decreasing = True

        prev = int(number)

    if increasing and decreasing:
        logging.debug(f"unsafe increasing and decreasing")
        safe = False
    if safe:
        safecount += 1

logging.info(f"{safecount} safe rows found")


print(f"{safecount} safe rows")
