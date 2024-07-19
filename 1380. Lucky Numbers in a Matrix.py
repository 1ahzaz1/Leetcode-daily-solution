class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        #This is O(m * n) complexity
        #We iterate over every element in the matrix (O(m*n) in first nested for loop)
        #We also iterate over 1 element (indexed) from every row again (seperate nested for loop)
        lucky_nums = []

        #Loop through each row and find its minimum + index of min
        for row in matrix:
            min_from_row = row[0]
            for i in range(len(row)):
                if row[i]<=min_from_row:
                    min_from_row = row[i]
                    column = i
            is_max = True
            #Loop through every other row in the same index (=column)
            for j in range(len(matrix)):
                if matrix[j][column] > min_from_row:
                    is_max = False
            #If theres no greater number in that column, we can append to output
            if is_max:
                lucky_nums.append(min_from_row)

        return lucky_nums

        