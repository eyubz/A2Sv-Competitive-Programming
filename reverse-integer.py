class Solution:
    def reverse(self, x: int) -> int:
        rem=0
        num=0
        limit=[pow(-2,31), pow(2,31)]
        negative=False
        if x<0:
           negative=True
           x=-(x)
        while x>0:
            rem=x%10
            x//=10
            num=num*10+rem
        if num not in range(limit[0],limit[1]):
            return 0
        elif negative:
            return -(num)
        return num
