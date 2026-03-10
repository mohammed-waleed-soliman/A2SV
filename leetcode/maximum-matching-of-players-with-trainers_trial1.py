class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j = 0
        res = 0
        for i in range(len(players)):
            if j>=len(trainers):
                break
            while players[i]>trainers[j]:
                j+=1
                if j==len(trainers):
                    return res
            res+=1
            j+=1
        return res