class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i==0 or flowerbed[i-1]==0) and (flowerbed[i+1]==0 or i == len(flowerbed)-1):
                flowerbed[i] = 1
                count+=1
            i+=1
        return count>=n


sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1],1))