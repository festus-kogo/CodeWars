def high_and_low(numbers):

    nums = [int(x) for x in numbers.split()]
    return str(max(sorted(nums))) + " " + str(min(sorted(nums)))

print(high_and_low("1 2 3 4 5")) # 5 1

print(high_and_low("1 2 -3 4 5")) # 5 -3

print(high_and_low("1 9 3 4 -5")) # 9 -5

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")) # 42 -9
