class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        n = len(events)
        events.sort(key=lambda x: x[0])
        suffix_max = [events[-1][2]] * len(events)

        value_max = 0
        #Track the suffixMax reward value
        #This way we can grab the best value from the index of the first valid second interval
        for j in range(n-2, -1, -1):
            suffix_max[j] = max(suffix_max[j+1], events[j][2])
        
        for i in range(n):
            value1 = events[i][2]
            value2 = 0
            target = events[i][1] + 1
            lo, hi = i + 1, n
            #Binary search remaining interval for the first valid second interval
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if events[mid][0] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            if lo < n:
                value2 = suffix_max[lo] #SuffMax saves us from going through the rest of the list
            value_max = max(value_max, (value1 + value2))

        return value_max