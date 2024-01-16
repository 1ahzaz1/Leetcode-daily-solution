class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []  #we need this class to have an underlying array for O(1) get random

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)  #maps each val to its index in underlying array
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:   #to remove from array in O(1), swap val with last position and pop
        if val not in self.dict:
            return False
        last_element = self.list[-1]
        index = self.dict[val]  #dict values map to their index in the underlying array
        self.list[index], self.list[-1] = last_element, val #swap with last
        self.dict[last_element] = index #update index of last
        self.list.pop()
        del self.dict[val]  #remove from set is O(1)
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)  #O(1) if we get the random from
