nums = [12,34,56,78,90]
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
print(smallest)