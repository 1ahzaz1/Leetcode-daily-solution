class Solution:
    def countPermutations(self, complexity: List[int]) -> int:

        smallest = complexity[0]

        #Check if any complexity[i] > the first unlocked computer,
        #In which case it's  impossible to unlock all.
        for i in range(1, len(complexity)):
            if complexity[i] <= smallest:
                return 0

        perms = math.factorial(len(complexity)-1)
        #Since all of these can be unlocked by complexity[0],
        #We can unlock the computers in any/every order, using complexity[0] for all of them
        #Note, len(complexity)-1, as complexity[0] will ALWAYS be unlocked first.
        mod = (10**9) + 7
        return perms%mod
        