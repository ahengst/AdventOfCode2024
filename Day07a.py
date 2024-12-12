# Day 07

# Algorithm / Python topics used today
#    use regex to...

# learned...
#   passing a list to a function is like passing a pointer to the list
#   the function can change the list, and the changes are reflected in the calling function
#        To preserve the original list, make a copy of it before passing it to the function
#        Or have the function make a copy of the list before changing it
#   thing2
#


import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

DIGITS = "0123456789"

FNAME = "Day07atest.txt"
FNAME = "Day07a.txt"


grandtotals_a = 0
listn = []

with open(FNAME) as f:
    for line in f:
        logging.debug(f"line raw: {line}")
        testv, listn = line.strip().split(":")
        testv = int(testv)
        listn = listn.strip().split(" ")
        for i, nn in enumerate(listn):
            listn[i] = int(nn)
        logging.debug(f"testv {testv} listn {listn}")

        # Let's pretend it's always 5 numbers.  4 operators.
        listlen = len(listn)
        # set list operators[] to listlen-1 "+"s
        operators = ["+"] * (listlen - 1)
        combos = 2 ** (listlen - 1)
        for opcombo in range(combos):
            t = listn[0]
            for i, op in enumerate(operators):
                if op == "+":
                    t += listn[i + 1]
                else:
                    t *= listn[i + 1]
            if t == testv:
                grandtotals_a += testv
                logging.debug(f"grandtotals_a {grandtotals_a}  operators {operators}")
                # no need to try different operator combinations
                break
            # keep trying, after binary-increment of operators list
            for i in range(len(operators)):
                if operators[i] == "+":
                    operators[i] = "*"
                    break
                else:
                    operators[i] = "+"
            logging.debug(f"new list of operators {operators}")


logging.info(f"{grandtotals_a} and other info")

print(grandtotals_a)
