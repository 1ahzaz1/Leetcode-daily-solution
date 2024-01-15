class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        losses = {} #to store the losers and their loss totals
        players = set() #to store unique players

        for match in matches:
            players.add(match[0]) #add winner to set
            players.add(match[1]) #add loser to set

            if match[1] not in losses:  #adds new player to loss dict with 1 loss value
                losses[match[1]] = 1
            else:
                losses[match[1]] +=1  #increments the value(losses) in the key(player) since they already lost before

        no_loss = [player for player in players if player not in losses] #gets unique players not in losses
        one_loss = [player for player, loss in losses.items() if loss == 1] #gets all players from losses where value=1

        return [sorted(no_loss), sorted(one_loss)] #sorted makes it not simply O(n). but still most efficient