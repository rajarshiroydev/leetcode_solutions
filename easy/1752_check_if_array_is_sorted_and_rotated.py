class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0

        '''
        logic: if there are more than one drop in value in adjacent elements then
        the array was never sorted in the initial state. so we are just checking
        the count of drop in values between consecutive elements.
        '''
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1

        '''
        this is to handle the comparison between last and the first element
        because the arrays are rotated.
        '''
        if nums[len(nums) - 1] > nums[0]:
            count += 1

        if count > 1:
            return False
        else:
            return True
