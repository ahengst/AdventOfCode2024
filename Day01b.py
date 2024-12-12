# Day01b.py

# Algorithm / Python topics used today
#   convert input COLUMNS into python LISTS

# learned...
#   sort a list: list.sort() or sorted(list)


import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")


FNAMEL = "Day01L.txt"
FNAMER = "Day01R.txt"
MAX = 1000
FNAMEL = "Day01testL.txt"
FNAMER = "Day01testR.txt"
MAX = 6


infileL = open(FNAMEL)  # opens file for (default=read)
infileR = open(FNAMER)  # opens file for (default=read)


indexL = 0
indexR = 0
SimilarityScore = 0
# Assume all numbers in ascending order in each file.
# read first line from infileR
lineR = infileR.readline()
indexR += 1
logging.debug(f"First lineR = {lineR} at idx {indexR}")

prevLineL = "0000"
while indexL < MAX:
    lineL = infileL.readline()
    indexL += 1
    logging.debug(f"Checking L= {lineL} at idx {indexL}")

    if lineL == prevLineL:
        # found duplicate lines in file L, increment SimilarityScore and read next line from infileL
        SimilarityScore += LineSimilarity
        logging.debug(
            f"   found duplicate lineL = {lineL} and score is {SimilarityScore}"
        )
        continue

    prevLineL = lineL
    # check file R to find the matching line(s)
    LRhits = 0

    while lineR < lineL:
        # if lineR is small, read next line from infileR
        lineR = infileR.readline()
        indexR += 1
        logging.debug(f"   new lineR = {lineR} at idx {indexR}")
    while lineR == lineL:
        # if lineR is equal to lineL, increase the hit count and read next line from infileR
        LRhits += 1
        logging.debug(f"   HIT lineR = {lineR} at idx {indexR} so read another")
        lineR = infileR.readline()
        indexR += 1

    logging.debug(f"   found too big lineR = {lineR} at idx {indexR}")
    # at this point we tally the hit count for this lineL

    logging.info(f"Row L {lineL} had {LRhits} hits in file R")
    LineSimilarity = int(lineL) * int(LRhits)
    SimilarityScore += LineSimilarity
    logging.debug(f"score increases by{lineL}*{LRhits}")
    logging.debug(f"score is {SimilarityScore}")


print(f"the total SimilarityScore is {SimilarityScore}")
