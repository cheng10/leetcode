class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2: return len(nums)
        tail = 0
        for i in range(len(nums)):
            if nums[tail]!= nums[i]:
                tail +=1 
                nums[tail] = nums[i]
 
        return tail + 1
