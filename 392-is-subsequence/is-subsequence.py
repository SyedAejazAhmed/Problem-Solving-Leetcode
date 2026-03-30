class Solution:
    def isSubsequence(self, s, t):
        s_i, t_i = 0, 0
        
        while s_i < len(s) and t_i < len(t):
            s_i, t_i = s_i + (s[s_i] == t[t_i]), t_i + 1
            
        return s_i == len(s)