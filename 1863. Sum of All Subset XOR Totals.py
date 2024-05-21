class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        #Below is O(n) solution using maths
        #Firstly we find all the columns where in atleast one bit represestation of the input numbers occurs a 1
        #We can do this by finding the 'OR' of all numbers in input
        ones = 0
        for num in nums:
            ones = ones | num

        #Wherever the 1's appear in ones, in all the 2^nums subsets;
            #Half of them will include a 1 in that position after xor all in subset
            #IE 2**nums-1
        #Therefor we dont even need to convert ones to binary representation
        return ones * 2**(len(nums)-1)