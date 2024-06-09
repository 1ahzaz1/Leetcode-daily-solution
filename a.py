class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        #store the frequency of remainders
        # Start with {0: 1} to handle the case where a prefix sum itself is divisible by k
        remainder_map = {0: 1}
        
        #keep track of the cumulative sum
        prefix_sum = 0
        
        #keep track of the number of subarrays that are divisible by k
        count = 0
        
        # Iterate through each number in the input list
        for num in nums:

            prefix_sum += num
            
            remainder = prefix_sum % k
            
            # Adjust remainder to be positive if it is negative
            if remainder < 0:
                remainder += k
            
            # If the remainder has been seen before, it means there are subarrays ending at the current index which are divisible by k
            if remainder in remainder_map:
                # Add the count of such subarrays to the result
                count += remainder_map[remainder]
                
                remainder_map[remainder] += 1
            else:
                # If the remainder is not seen before, add it to the map with a count of 1
                remainder_map[remainder] = 1
        
        return count
