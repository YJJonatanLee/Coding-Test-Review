from math import factorial

class Solution(object):
    def getPermutation(self, n, k):
        output = ''
        nums_list = [str(i) for i in range(1,n+1)]
        
        for i in range(n-1,-1,-1):
            devide = factorial(i)
            pos = (k-1) // devide
            output += nums_list[pos]
            nums_list.pop(pos)
            k %= devide
        
        return output
