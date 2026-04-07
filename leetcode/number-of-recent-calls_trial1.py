class RecentCounter:

    def __init__(self):
        self.ind = 0
        self.req = []

    def ping(self, t: int) -> int:
        self.req.append(t)
        while (self.req[-1]-self.req[self.ind])>3000:
            self.ind+=1
        return len(self.req)-self.ind


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)