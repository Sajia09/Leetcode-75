class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j= len(s)-1
        s= list(s)
        while i<j :
            if s[i] in 'AEIOUaeiou' and s[j] in 'AEIOUaeiou':
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
            elif s[i] in 'AEIOUaeiou':
                j-=1
            else:
                i+=1
        return"".join(s)
sol = Solution()
print(sol.reverseVowels("leetcode"))