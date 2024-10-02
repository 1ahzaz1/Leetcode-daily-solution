class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        val_to_rank = {} #Hashmap to map different nums from arr to their ranks (main part)

        clean_arr = sorted(list(set(arr))) #Convert arr to set and back to remove duplicates, then sort. O(N+N+NLOGN) = O(nlogn)

        for i in range(len(clean_arr)):
            num = clean_arr[i]
            val_to_rank[num] = i+1 #Thus completing the mapping of unique nums to their rank
        
        for i in range(len(arr)):
            num = arr[i]
            arr[i] = val_to_rank[num] #Gets value(rank) from key(num in array). Repeat lookups of same key is fine(duplicates problem)

        return arr




