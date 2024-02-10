
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:

        n = len(candies)
        out_list =[True]*n
        for i in range(n):
            if candies[i]+extraCandies < max(candies):
                out_list[i]= False
        return out_list

sol = Solution()
print(sol.kidsWithCandies([2,3,5,1,3],3))