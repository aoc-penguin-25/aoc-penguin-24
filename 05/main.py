from collections import defaultdict
from turtle import update

rule_dict: dict[int, dict[int,bool]] = defaultdict(lambda: defaultdict(lambda: False))

# make the dep graph
# maybe make the transitive dep graph
def make_rule_dict(rules:str):
    # print(rules)
    for i in range(100):
        rule_dict[i] = defaultdict(lambda: False)
    for rule_line in rules.splitlines():
        page_before, page_after = rule_line.split("|")
        rule_dict[int(page_before)][int(page_after)] = True
    return rule_dict

def deps_within_update(num:int, update_list:list[int]):
    other_pages = update_list.copy()
    other_pages.remove(num)
    deps = 0
    for other_page in other_pages:
        if rule_dict[num][other_page]:
            deps += 1
    return deps


def find_right_middle_number(update_numbers:list[int]):
    # print("wrong: " + ",".join(map(str,update_numbers)))
    copied_list = update_numbers.copy()
    update_numbers.sort(key = lambda n: deps_within_update(n, copied_list))
    return update_numbers[len(update_numbers) //  2]

with open("05/input.txt", encoding="utf-8") as f:
    sections = f.read().split("\n\n")
    rule_lines = sections[0]
    rule_dict = make_rule_dict(rule_lines)
    update_lines = sections[1].strip().splitlines()
    # print(update_lines)
    correct_middle_page_sum = 0
    incorrect_middle_page_sum = 0
    for update_line in update_lines:
        update_numbers = list(map(int, update_line.split(',')))
        middle_number = update_numbers[len(update_numbers) // 2]
        # walk back through the pages
        line_safety = True
        # print(update_numbers)
        for i in range(len(update_numbers) -1 ,1, -1):
            # check if it breaks a rule
            # print(str(i))
            for j in range(i):
                # print("#" +str(j))
                if rule_dict[update_numbers[i]][update_numbers[j]]:
                    line_safety = False
                    # print(str(i) + " should have been before: " + str(j))
        if line_safety:
            correct_middle_page_sum += middle_number
        else:
            incorrect_middle_page_sum += find_right_middle_number(update_numbers)
    print(correct_middle_page_sum)
    print(incorrect_middle_page_sum)