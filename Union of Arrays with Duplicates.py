class Solution:    
    def findUnion(self, a, b):
        result = list(set(a)|set(b))
        return result
