class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
    
        #n is between 1 and 100
        #Sorting before comparing O(nlogn)
        #Counting sort not required
        
        students = sorted(students)
        seats = sorted(seats)

        output = 0

        for i in range(len(students)):
            output += abs(students[i] - seats[i])
        return output