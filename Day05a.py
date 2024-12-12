# Day 05a.py

# AoC Stats for Day 5 - 30 people got the first star in the first minute.
# AoC Stats for Day 5 - 22 people got the both stars in the first 2 minutes.


# Algorithm / Python topics used today
#   Read test list of strings
#   For each list
#       test if every pair (written nn|mm) is in the list
#       if so, do the thing for good groups
#   For each bad list
#       rearrange it (new first member) until all rules are followed

# learned...
#   when continue and break don't work, a boolean flag is useful
#   debug was necessary - maybe use fewer logging statements?
#


import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

FNAME = "Day05atest1.txt"
FNAMEL = "Day05atest2.txt"
FNAME = "Day05a1.txt"
FNAMEL = "Day05a2.txt"


# read FNAME into list of strings
SORTlist = []
with open(FNAME) as f:
    for line in f:
        SORTlist.append(line.strip())

# read FNAMEL checking each group of pairs against SORTlist
midpagesuma = 0
midpagesumb = 0
with open(FNAMEL) as f:
    for line in f:
        logging.debug(f"line: {line}")
        goodgroup = True
        tests = line.strip().split(",")
        # while we're here grap the # in the middle of the group

        midp = tests[len(tests) // 2]

        while len(tests) > 1:
            logging.debug(f"  {tests[0]} and {tests[1]}")
            if tests[0] + "|" + tests[1] in SORTlist:
                tests.pop(0)
            else:
                goodgroup = False
                break
        if goodgroup:
            logging.debug(f"line group appears {goodgroup}")
            midpagesuma += int(midp)
        else:
            # We must sort the group so that all the pairs are in order
            # NewList = [] and append next # that must be before all others in this group
            NewList = []
            tests = line.strip().split(",")
            # tests [] is in some order but we will rearrange and pop() as we go
            while len(tests) > 1:
                goodorder = True
                # are there rules that put each OTHER page after this one?
                for t in tests[1:]:
                    if tests[0] + "|" + t in SORTlist:
                        logging.debug(f" {tests[0]} and {t} are in order")
                    elif t + "|" + tests[0] in SORTlist:
                        logging.debug(f"  {tests[0]} and {t} in REVERSE order")
                        # set up for a retest...
                        tests.append(tests.pop(0))
                        goodorder = False
                        break
                    else:
                        logging.debug(
                            f" {tests[0]} and {t} order is unknown keep going"
                        )

                if goodorder:
                    NewList.append(tests.pop(0))
            # and the last one as well
            NewList.append(tests.pop(0))

            logging.debug(f"NewList: {NewList} should be in good order")

            # Now we can check the NewList for the middle #
            midp = NewList[len(NewList) // 2]
            midpagesumb += int(midp)

logging.info(f"{midpagesuma} and {midpagesumb}")

print(midpagesumb)
