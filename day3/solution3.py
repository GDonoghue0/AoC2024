import re

with open("input3.txt", "r") as f:
    data = ''.join([line.strip() for line in f])


def sum_all_mults(data):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    instructions = pattern.findall(data)

    total = 0
    for a,b in instructions:
        total += int(a) * int(b)

    return total


def handle_conditionals(data):
    do_str = "do()"
    dont_str = "don't()"

    data_copy = ""
    enable = True
    for i in range(len(data)-7):
        if enable:
            data_copy += data[i]
        if data[i:i+4] == do_str:
            enable = True
        if data[i:i+7] == dont_str:
            enable = False
    return data_copy

data_copy = handle_conditionals(data)
print(sum_all_mults(data_copy))