from collections import Counter

# get lists out of the file.
def list_extractor():
    # initialize empty left and right lists
    left_list = []
    right_list = []

    # read each line of input.txt in the same folder as this file
    with open("01/input.txt") as f:
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


# solves for part 1
def part1():
    ## get lists
    left_list, right_list = list_extractor()

    # sort the lists
    left_list.sort()
    right_list.sort()

    # initialize the sum counter
    sum = 0
    # lazy incantation to iterate over the two lists zippered up.
    # really trusting that they're the same length.
    for left, right in zip(left_list, right_list):
        # add the diff between them to the sum.
        sum += abs(left - right)

    print("part 1 is: ", sum)

def part2():
    # so I read the story as "value of number" x "right count" x "left count"

    ## get lists
    left_list, right_list = list_extractor()

    ## count it all up. note - Counter gives 0 instead of errors on failed lookups.
    left_counter = Counter(left_list)
    right_counter = Counter(right_list)

    # init a sum
    sum = 0

    # go thru everything in left list
    for entry in left_counter:
        # add up the value of the number * occurance in left * occurance in right
        sum += entry * left_counter[entry] * right_counter[entry]

    # no need to go thru right as well, since it would be *0 with left.

    print("part 2 is: ", sum)

part1()
part2()
