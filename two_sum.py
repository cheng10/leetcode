class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for indexi, i in enumerate(nums):
            for indexj, j in enumerate(nums[indexi+1:]):
                if i+j == target:
                    result = [indexi, indexj+indexi+1]

        return result
