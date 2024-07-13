class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove_substring(input, first, second, points):
            #Helper function to remove substring given order (ab or ba) as stack, and return points gained + new string

            stack = []
            score = 0
            for char in input:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

        #Remove from string in ab or ba first, depending on which gives more points
        if x>y:
            s, score1 = remove_substring(s, 'a', 'b', x)
            s, score2 = remove_substring(s, 'b', 'a', y)
        else:
            s, score1 = remove_substring(s, 'b', 'a', y)
            s, score2 = remove_substring(s, 'a', 'b', x)
        
        return score1+score2