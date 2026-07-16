class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i,x in enumerate(nums):
            for j,y in enumerate(nums[i+1:]):
                if x==y:
                    return True
        return False