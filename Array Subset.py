#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        freqa = dict()
        freqb = dict()
        for i in a:
            if i in freqa:
                freqa[i] += 1
            else:
                freqa[i]=1
        
        for i in b:
            if i in freqb:
                freqb[i] += 1
            else:
                freqb[i]=1
        
        for key in freqb:
            if not (key in freqa):
                return False
            if freqb[key]>freqa[key]:
                return False
        
        return True
    
    
    
