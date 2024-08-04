class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        #Can always be made equal if they have the same numbers in each array
        #This is because we can swap 2 adjacent like bubble swap
        #By doing this, we can move any element anywhere without affecting others

        numset = {}

        for num in arr: #Go over nums in array and create dict storing each + their occurrences
            if num in numset:
                numset[num] +=1
            else:
                numset[num] = 1
        #Go over nums in target, if it has same nums and occurrences of each, then its possible

        for num in target:
            if num in numset:
                if numset[num] == 0:
                    return False
                else:
                    numset[num] -=1
            else:
                return False
        return True
