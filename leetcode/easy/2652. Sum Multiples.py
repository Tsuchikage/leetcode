class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        for i in range(n):
            if (i + 1) % 3 == 0 or (i + 1) % 5 == 0 or (i + 1) % 7 == 0:
                sum += i + 1
            
        return sum
