class Solution:
    def reverse(self, x: int) -> int:
        MAX_NUM = 2**31 - 1
        SIGN = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            if rev > (MAX_NUM - digit) // 10:
                return 0
            rev = rev * 10 + digit
        return SIGN * rev        