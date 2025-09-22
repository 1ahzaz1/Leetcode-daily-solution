class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        total_freq = {}
        # First count the frequency of each number
        for num in nums:
            if num in total_freq:
                total_freq[num] += 1
            else:
                total_freq[num] = 1
        max_freq = 0
        num_max_freq = 0
        # Then find the maximum frequency and count how many numbers have that frequency
        for freq in total_freq.values():
            if freq > max_freq:
                max_freq = freq
                num_max_freq = 1
            elif freq == max_freq:
                num_max_freq +=1
        # Finally, return the product of the maximum frequency and the count of numbers with that frequency
        return max_freq * num_max_freq