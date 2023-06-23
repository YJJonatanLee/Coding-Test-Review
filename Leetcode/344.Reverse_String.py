class Solution:
    def reverseString(self, s):
        l = 0
        r = len(s) - 1
        
        def reverse(l, r, s):
            # 왼쪽과 오른쪽이 만나면 종료
            if l >= r:
                return s
            
            else:
                # 왼쪽과 오른쪽을 바꿔주고
                s[l], s[r] = s[r], s[l]
                # pointer를 한 칸 씩 옮겨 재귀
                return reverse(l+1, r-1, s)
        
        return reverse(l, r, s)
