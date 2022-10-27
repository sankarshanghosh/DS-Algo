nums = [1, 2, 1]
ans = [0] * (2 * len(nums))

for i in range(0, len(nums)):
    ans[i] = nums[i]
    ans[i + len(nums)] = nums[i]
print(ans)