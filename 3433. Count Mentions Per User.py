class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        for k in range(len(events)):
            if events[k][0] == "MESSAGE":
                events[k][0] = "BESSAGE"
            elif events[k][0] == "OFFLINE":
                events[k][0] = "AFFLINE"
        events.sort(key=lambda x : (int(x[1]), x[0]))
        mentions = [0] * numberOfUsers

        cooldown = [0] * numberOfUsers
        currTime = 0

        for event in events:
            print(event, mentions)
            timePassed = int(event[1]) - currTime
            for i in range(len(cooldown)):
                cooldown[i] -= timePassed
                if cooldown[i]<0:
                    cooldown[i] = 0

            if event[0] == "BESSAGE":
                for person in event[2].split(" "):
                    if person == "HERE":
                        for i in range(numberOfUsers):
                            if cooldown[i] == 0:
                                mentions[i] += 1
                    elif person == "ALL":
                        for j in range(len(mentions)):
                            mentions[j] += 1
                    else:
                        user = int(person[2:])
                        mentions[user] += 1
            
            elif event[0] == "AFFLINE":
                cooldown[int(event[2])] = 60
            currTime = int(event[1])
        return mentions
 