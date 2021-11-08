def is_monotonic(nums):
    vozr = sorted(nums)
    ubiv = sorted(nums, reverse = True)
    if nums != vozr and nums != ubiv:
        return False
    else:
        return True
