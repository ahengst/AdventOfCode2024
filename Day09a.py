# Day 09a

# Algorithm / Python topics used today
#    THIS BROKE WHEN I COMPLETELY REWROTE IT FOR PART 2 before copying Day09b.py to Day09a.py
#    using slightly abstracted 2-list datastructure, not an actual disk map table.

# learned...
#   thing1
#   thing2
#

# Copilot came up with these on its own:
#   blablabla

import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
# logging.critical / .error / .warning / .info / .debug(f"..")

DIGITS = "0123456789"

FNAME = "Day09atest2.txt"
FNAME = "Day09a.txt"
FNAME = "Day09atest.txt"

# Problem interpretation 1: WRONG
#    The file ID is a single digit, rotating from 0 to 9 endlessly.
# Problem interpretation 2:
#    The file ID is a growing sequence, use as many occurrences as needed to reach X characters
# Problem interpretation 3:
#    The file ID is a growing sequence, use as many occurrences as requested even multi-digit numbers
# Problem interpretation 4:   DOING THIS ONE
#    Instead of digits, allow block to contain integers of any size

# The "Disk Map" is the input data,

# a list of numbers representing block values, zero for empty space.
datablocks = []
freeblocks = []

idn = 0

# read file two characters at a time
# &&& try reading the entire file in, then process the chars
print(f"Reading file {FNAME}")
data = open(FNAME).read().strip()
disk_map = [int(n) for n in data]

print(f"separating files and free space")
blockpos = 0
fid = 0
for idn, [c, s] in enumerate(zip(disk_map[::2], disk_map[1::2])):
    # do the "file" character
    # c = f.read(1)
    # if not c:
    #    logging.info(f"C? found EOF")
    #    break

    # logging.debug(f"C found {c}")
    # this is interpretation 4:   add c occurrences of idn (as int) to blocks
    if int(c) > 0:
        datablocks.append([blockpos, fid, int(c)])
        blockpos += int(c)
    fid += 1

    # do the "spaces" characters
    # s = f.read(1)
    # if not s:
    #     # this is the end of the file
    #     logging.info(f"S? found EOF")
    #     break
    # elif s == "\n":
    #     logging.info(f"S? found Newline")
    #     break
    # logging.debug(f"S found {s}")
    # fs.append("." * int(s))
    if int(s) > 0:
        freeblocks.append([blockpos, int(s)])
        blockpos += int(s)
    logging.debug(f"freeblocks: {freeblocks}")
# And the final datablock
logging.debug(f"datablocks: {datablocks}")
datablocks.append([blockpos, fid, int(disk_map.pop())])
logging.debug(f"datablocks: {datablocks}")
blockpos += int(c)

# The datablocks list is a list of 3-tuples, each tuple is the position(ascending), the file ID and the number of blocks in that file.
# The freeblocks list is a list of 2-tuples, each tuple is the position(ascending), and the number of free blocks at that position.


print(f"Compacting the disk")

# datablocks do not need to be in order, but [0] position is important
# freeblocks order is important

# locate a big-enough block of free space
#     find next free block of size >= file size
# if we find an exact gap, remove the freespace block.
#     insert a file block, remove a fileblock
# if we find a gap, but not exact, shorten AND reindex a freespace block.
#     update the free block: index+= movedblocklength
for dblock in datablocks[::-1]:
    # stop when current datablock is before first free block
    if dblock[0] < freeblocks[0][0]:
        logging.info(
            f"stopping at dblock {dblock} because #1 freeblock is {freeblocks}"
        )
        break
    # last datablock[] first, until all have been checked
    moved_blocks = []
    for dig in range(dblock[2]):
        # fill an individual free block (until it's full)
        #  ...by appending moved_blocks from the datablock
        for fblock in freeblocks:
            if fblock[1] >= dblock[2]:
                # update dblock position
                dblock[0] = fblock[0]
                # shorten or remove the free block
                if fblock[1] == dblock[2]:
                    # exact match, remove the free block
                    freeblocks.remove(fblock)
                else:
                    # shorten the free block
                    fblock[0] += dblock[2]
                    fblock[1] -= dblock[2]
                break  # no need to check more free blocks


# fstring = "".join(flist).strip()
logging.debug(f"flist: {datablocks}")

print(f"Calculating Part 1 checksum")
# calculate filesystem checksum
# The datablocks list is a list of 3-tuples, each tuple is the position(ascending), the file ID and the number of blocks in that file.
csum = 0
# new checksum calculation
for i, dblock in enumerate(datablocks):
    offs = dblock[0]  # block offset
    for n in range(dblock[2]):
        csum += (dblock[0] + n) * dblock[1]
        logging.debug(f"i {i} fid {dblock} offs {offs} n {n} csum {csum}")
    logging.debug(f"interim checksum {csum} at i {i}")

print(f"fs checksum {csum}")
# PART 1 Answer attempts
# 5672833528 is too low
# 89914538143 is too low
# 6340197768906   is correct (interpretation 4)

# PART 2 Answer attempts
# 6725534328962 is too high        If the last-moved file could be moved even a little, it would be a better answer.

# Read the solution code at https://www.reddit.com/r/adventofcode/comments/1ha27bo/2024_day_9_solutions/
# optimize run time
