def distribute(banks):
    m = max(banks)
    idx = 0
    for i, val in enumerate(banks):
        if val == m:
            idx = i
            break
    banks[idx] = 0
    while m != 0:
       idx += 1
       idx %= len(banks)
       banks[idx] += 1
       m -= 1

def solve(banks, count_second):
    # Keep a set of seen states.
    seen = set()
    count = 0

    # Iterate until we get a repeat state.
    while tuple(banks) not in seen:
        seen.add(tuple(banks))
        distribute(banks)
        count += 1
    # If we're going to count the secondary iterations, then recurse.
    if count_second:
        # Get the count starting anew from the last state.
        return solve(banks, False)
    # Otherwise, return the desired count.
    else:
        return count

with open('Day6.txt') as inp:
    banks = list(map(int,inp.read().strip().split()))
    # Part 1.
    print(solve(banks, False))
    # Part 2.
    print(solve(banks, True))
