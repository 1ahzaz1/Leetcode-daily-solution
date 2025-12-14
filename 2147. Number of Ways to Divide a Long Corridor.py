class Solution:
    def numberOfWays(self, corridor: str) -> int:

        seats = 0
        output = []
        i = 0
        MOD = 10**9 + 7

        if corridor.count("S") == 0 or corridor.count("S") % 2 == 1:
            return 0

        #Count how many plants are between any 2 seats for all their permutations
        #Then multiply these together for every single possible way
        while i < len(corridor):
            if corridor[i] == "S":
                seats += 1
                if seats == 2:
                    curr = 1
                    i += 1
                    while i < len(corridor) and corridor[i] == "P":
                        curr += 1
                        i += 1
                    if i < len(corridor):
                        output.append(curr)
                    seats = 0
                    continue
            i += 1


        finalOutput = 1
        for k in output:
            finalOutput = (finalOutput*k) %MOD
        return finalOutput
