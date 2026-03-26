class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0]*(n+2)
        for i in range(len(bookings)):
            arr[bookings[i][0]]+=bookings[i][2]
            arr[bookings[i][1]+1]-=bookings[i][2]
        for i in range(1,n+2):
            arr[i]+=arr[i-1]
        return arr[1:n+1]