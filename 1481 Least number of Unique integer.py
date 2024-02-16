from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        a = Counter(arr)
        b = sorted(a.values())
        n  = len(b)
        for count in b:
            if k >= count:
                k -= count
                n -= 1
            else:
                break
        return n
sol = Solution()
print(sol.findLeastNumOfUniqueInts([4,3,1,1,3,3,2],3))