import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

# part 1
with open("03/input.txt", encoding="utf-8") as f:
        matches = re.findall(pattern, f.read())
        accumulate_sum = 0
        for match in matches:
            accumulate_sum += int(match[0]) * int(match[1])
        print(accumulate_sum)

# part 2
with open("03/input.txt", encoding="utf-8") as f:
        accumulate_sum = 0
        content = f.read()
        dos = content.split("do()")
        for do in dos:
            till_dont = do.split("don't()")[0]
            matches = re.findall(pattern, till_dont)
            for match in matches:
                accumulate_sum += int(match[0]) * int(match[1])
        print(accumulate_sum)