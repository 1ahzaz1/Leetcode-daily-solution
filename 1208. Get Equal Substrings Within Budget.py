class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        curr_cost = 0
        max_length = 0

        for end in range(len(s)):
            # calculate the cost to change s[end] to t[end]
            curr_cost += abs(ord(s[end]) - ord(t[end]))

            #if the curr cost exceeds max cost, move the start pointer to reduce the cost
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            #calculate the max length of the valid window
            max_length = max(max_length, end - start + 1)
        
        return max_length