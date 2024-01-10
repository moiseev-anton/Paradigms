def sort_imperative(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        curr = nums[i]
        j = i - 1
        while j >= 0 and curr > nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = curr
    return nums


def sort_declarative(nums: list[int]) -> list[int]:
    return sorted(nums, reverse=True)


nums = [9, 3, 1, 5, 7, 4]
print(sort_imperative(nums))
print(sort_declarative(nums))
