class Solution:
    def romanToInt(self, s: str) -> int:
        r_i = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        ans = 0
        for i in range(len(s) - 1):
            ch = s[i]
            nxt_ch = s[i + 1]
            if r_i[ch] >= r_i[nxt_ch]:
                ans += r_i[ch]
            else:
                ans -= r_i[ch]
        ans += r_i[s[len(s)-1]]
        
        return ans