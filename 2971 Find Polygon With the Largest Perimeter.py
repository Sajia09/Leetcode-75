class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        sum = 0
        perimeter = -1

        for num in nums:
            if num< sum:
                perimeter = num + sum
            sum += num
        return perimeter
sol = Solution()
print(sol.largestPerimeter([1,12,1,2,5,50,3]))

# 1,1,2,3,5,12,50