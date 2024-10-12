def app(nums):
    nums.sort()
    count = 1
    for i in range(len(nums)):
        try:
            if abs(nums[i+1] - nums[i]) > 1:
                break
            if abs(nums[i+1] - nums[i]) == 0:
                continue
            else:
                count += 1
        except Exception as e:
            continue

    return count


nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 10, 11, 12, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23, 24, 25, 25, 26, 27, 28, 29, 30, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
res = app(nums)
print(res)
print(nums)
