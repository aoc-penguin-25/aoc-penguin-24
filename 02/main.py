"""Main solving AoC2024 Day 2"""


def check_levels(part2: bool = False):
    """Check if levels are safe."""
    
    with open("02/input.txt", encoding="utf-8") as f:
        lines = f.readlines()
        safe_count = 0
        for line in lines:
            numbers: list[int] = list(map(int, line.split()))
            if safety_check(numbers):
                safe_count += 1
                print("the safest level ever!")
            else:
                if not part2:
                    break
                # ok we gotta permutate.
                for i in range(len(numbers)):
                    extra_life = numbers.copy()
                    # just remove one lil tiny element
                    del extra_life[i]
                    if safety_check(extra_life):
                        safe_count += 1
                        print("got it eventually!")
                        break
                print("nah, that level was a bad idea")

        print(safe_count)

def safety_check(numbers: list[int]):
    level_may_be_safe = True
    diffs: list[int] = []
    positive_diff = 0
    print(numbers)
    for left, right in zip(numbers, numbers[1:]):
        diffs.append(left - right)
    print(diffs)
    for diff in diffs:
        if abs(diff) > 3 or abs(diff) == 0:
            level_may_be_safe = False
        if diff > 0:
            positive_diff += 1
            print("positive difference, gotta hope they're all positive.")
    if positive_diff > 0 and positive_diff < len(diffs):
        level_may_be_safe = False
        print("alternating is bad, totally unsafe.")
    if level_may_be_safe:
        print("still safe!")
        return True
    else:
        print("not safe")
        return False

check_levels(part2=True)
