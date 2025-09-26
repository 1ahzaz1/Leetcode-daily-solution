class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        n = len(triangle)
        # start from the bottom row as our initial DP
        best_to_bottom = triangle[-1][:]

        # walk upwards, collapsing the triangle row by row.
        for row in range(n - 2, -1, -1):
            next_best = [0] * (row + 1)
            current_row = triangle[row]

            for col in range(row + 1):
                # Two choices from (row, col): go down->left or down->right
                down_left = best_to_bottom[col]
                down_right = best_to_bottom[col + 1]
                best_child = down_left if down_left <= down_right else down_right

                next_best[col] = current_row[col] + best_child

            # Move up one level
            best_to_bottom = next_best

        return best_to_bottom[0]
