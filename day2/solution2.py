def is_monotonic(lst):
    diffs = [b - a for a, b in zip(lst, lst[1:])]
    if all(1 <= abs(d) <= 3 for d in diffs):
        if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
            return True
    return False

def can_be_monotonic(lst):
    for i in range(len(lst)):
        modified = lst[:i] + lst[i+1:]
        if is_monotonic(modified):
            return True
    return False

with open('input2.txt') as f:
    reports = [list(map(int, line.split())) for line in f if line.strip()]

safe_count = sum(is_monotonic(report) or can_be_monotonic(report) for report in reports)
print(safe_count)
