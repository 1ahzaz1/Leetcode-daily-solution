class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        pairing = [(names[i], heights[i]) for i in range(len(heights))]
        pairing.sort(key=lambda x: x[1], reverse=True)
        sorted_names = [name for name, height in pairing]
        return sorted_names