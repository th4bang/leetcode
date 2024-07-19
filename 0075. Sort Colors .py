class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zer = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)

        nums[: zer + 1] = zer * [0]
        nums[zer : zer + one + 1] = one * [1]
        nums[zer + one :] = two * [2]

'''
Difficulty: Medium
Runtime: 35ms
Beats: 74.09%
Complexity: O(n)
Submitted: 17,Jul,2024 
'''
        
        