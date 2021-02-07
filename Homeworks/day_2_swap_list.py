nums = [1,2,3,4,5,6]
nums_length = len(nums) // 2
swapped_list = nums[nums_length:] + nums[:nums_length]
print(swapped_list)
