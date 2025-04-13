class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        mod = 10**9 + 7

        num_even_positions = (n + 1) // 2
        num_odd_positions = n // 2

        even_part = pow(5, num_even_positions, mod)
        odd_part = pow(4, num_odd_positions, mod)

        return (even_part * odd_part) % mod
