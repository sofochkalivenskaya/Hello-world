def find_missing_nums(nums):
    n = max(nums)
    list = [i for i in range(1, n + 1) if i not in nums]
    return print(list)
