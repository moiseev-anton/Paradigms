def binary_search(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

if __name__ == "__main__":
    nums = [0, 2, 3, 5, 8, 9, 12, 16, 20, 24]
    result = binary_search(nums, 2)
    print(result)

