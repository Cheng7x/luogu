nums = [3, 1, 4, 1, 5, 9, 2, 6,]

import random
class Solution:
    def partition(self, nums, left, right):
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[left] = nums[left], nums[pivot_index]

        pivot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            # j 先动能保证交换时不越界 j 不会与 pivot 换
            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[left] = nums[left], nums[i]
        return i
    
    def quick_sort(self, nums, left, right):
        if left < right:
            pivot_index = self.partition(nums, left, right)
            self.quick_sort(nums, left, pivot_index - 1)
            self.quick_sort(nums, pivot_index + 1, right)
        return nums
    
    def sortArray(self, nums):
        return self.quick_sort(nums, 0, len(nums) - 1)
   
print(Solution().sortArray(nums))
    

