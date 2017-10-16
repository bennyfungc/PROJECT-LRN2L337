
class Solution(object):
    def findComplement(self, num):
        x = 0

        while x < num:
            x = (x << 1) + 1

        return x - num
