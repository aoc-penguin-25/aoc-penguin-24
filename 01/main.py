"""Main solving AoC2024 Day 1"""

from collections import Counter


def list_extractor() -> tuple[list[int], list[int]]:
    """Get lists out of the file."""

    # initialize empty left and right lists
    left_list: list[int] = []
    right_list: list[int] = []

    # read each line of input.txt in the same folder as this file
    with open("01/input.txt", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            # extract two integers from a line of text
            # note - map is a magic thing that applies something to each element.
            # In this case just converting every piece of the split string to an integer.
            left, right = list(map(int, line.split()))
            # add them to the lists.
            left_list.append(left)
            right_list.append(right)
    return left_list, right_list


def part1():
    """Solve for part 1."""

    ## get lists
    left_list, right_list = list_extractor()

    # sort the lists
    left_list.sort()
    right_list.sort()

    # initialize the sum counter
    sum_so_far = 0
    # lazy incantation to iterate over the two lists zippered up.
    # really trusting that they're the same length.
    for left, right in zip(left_list, right_list):
        # add the diff between them to the sum.
        sum_so_far += abs(left - right)

    print("part 1 is: ", sum_so_far)


def part2():
    """Solve for part 2."""pylint

    # so I read the story as "value of number" x "right count" x "left count"

    ## get lists
    left_list, right_list = list_extractor()

    ## count it all up. note - Counter gives 0 instead of errors on failed lookups.
    left_counter: Counter[int] = Counter(left_list)
    right_counter: Counter[int] = Counter(right_list)

    # init a sum
    sum: int = 0

    # go thru everything in left list
    for entry in left_counter:
        # add up the value of the number * occurance in left * occurance in right
        sum += entry * left_counter[entry] * right_counter[entry]

    # no need to go thru right as well, since it would be *0 with left.

    print("part 2 is: ", sum)


part1()
part2()
