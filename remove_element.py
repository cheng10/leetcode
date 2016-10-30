class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p = len(nums) -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums[i], nums[p] = nums[p], nums[i]
                p-=1
        return p+1
