class Solution:
    def removeDuplicates(self, s: str) -> str:
        output =""
        for i in range(len(s)):
            output+=s[i]
            while len(output)>=2 and output[-1]==output[-2]:
                output = output[:-2]
        return output