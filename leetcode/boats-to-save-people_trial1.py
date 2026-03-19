class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        i=0
        j=len(people)-1
        while i<=j:
            if people[j]<=limit:
                res+=1
                if i!=j:
                    if people[j]+people[i]<=limit:
                        i+=1
            j-=1
        return res