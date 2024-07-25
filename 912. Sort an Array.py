class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        #Mergesort solution
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2  #Find the mid of the array
                L = arr[:mid]  # Dividing the elements into 2 halves
                R = arr[mid:]

                merge_sort(L)  # Sort the first half
                merge_sort(R)  # Sort the second half

                i = j = k = 0

                #copy elements to temp arrays L[] and R[]
                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1

                # Checking if any element was left
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1

                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1

        merge_sort(nums)
        return nums
