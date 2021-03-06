__________________________________________________________________________________________________
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        a = [0] * n
        for i, j, k in bookings:
            a[i - 1] += k
            if j < n:
                a[j] -= k
        seats = 0
        for i in range(n):
            seats += a[i]
            a[i] = seats
        return a
__________________________________________________________________________________________________

__________________________________________________________________________________________________
