class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        money = {5:0, 10:0, 20:0}

        # Note; if we need to return 15 change, always better to try 10 + 5
        # before trying 5 + 5 + 5 as this is our only chance to use 10's
        # Thus saving the 5's for other bills eg 5 or 10 change with no 10s
        
        for bill in bills:
            money[bill] += 1
            change = bill - 5

            #Gave 20 and return 15
            if change == 15:

                if money[10] < 1: # We dont have a 10

                    if money[5] < 3: # We dont have a 5 5 5
                        return False
                    else: # We have a 5 5 5
                        money[5] -= 3
                else: # We have a 10
                    if money[5] > 0: # We have a 5 and a 10
                        money[10] -= 1
                        money[5] -= 1
                    else: # We have a 10 but no 5
                        return False


            #Gave 10 and return 5
            if change == 5:
                if money[5] < 1:
                    return False
                else:
                    money[5] -= 1
            print(money)
        return True
        
            
