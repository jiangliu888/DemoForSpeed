# coding:utf-8
def sumValue(nums,target):
    n = len(nums)
    left = 0
    right = n-1
    if n == 1:
        return False
    while(left<right):
        mid = left + (right-left+1)/2
        if nums[left] + nums[right] == target:
            return [left+1,right+1]
        elif nums[left] + nums[right] > target:
            right = mid
        else:
            left = mid
numbers = [2,7,11,15]
target = 13
print(sumValue(numbers,target))

