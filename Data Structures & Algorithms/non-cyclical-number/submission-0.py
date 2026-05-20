class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        while 1 not in results:
            num = 0
            for digit in str(n):
                num += int(digit)**2
            if num in results:
                return False
            results.add(num)
            n = num
        return True
        