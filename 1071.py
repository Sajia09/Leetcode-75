import math

class solution:
    def gcdOfStrings (self, str1:str, str2:str)-> str:
        gcd =""
        if(str1+str2 == str2+str1):
            n = math.gcd(len(str1),len(str2))
            for i in range(n):
                gcd+=str2[i]
            return gcd
        else:
             return ""

sol = solution()
print(sol.gcdOfStrings('LEFT','CODE'))