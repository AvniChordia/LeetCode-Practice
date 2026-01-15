class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        import sys
        sys.set_int_max_str_digits(6000)
        a=int(num1)
        b=int(num2)
        c=a+b
        return str(c)