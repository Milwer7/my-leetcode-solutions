class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i < len(nums):
            starting_value = nums[i]
            while j < len(nums): 
                if starting_value + nums[j] == target:
                    return [i, j]
                j+=1
            i+=1
            j=i+1