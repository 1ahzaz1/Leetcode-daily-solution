class Solution(object):
    def construct2DArray(self, original, m, n):

        # Check if the total elements are possible in output
        if n * m != len(original):
            return []
        
        output = []
        temp = []
        count = 0
        
        for val in original:
            temp.append(val)  # Add the current element to the temp row
            count += 1
            
            if count == n:  # If temp has enough elements for one row
                output.append(temp)  # Append the row to the 2D array
                temp = []  # Reset temp for the next row
                count = 0  # Reset the counter

        return output