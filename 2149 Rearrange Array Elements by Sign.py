class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:

        positive_num =[]
        negative_num =[]
        output =[]

        for num in nums:
            if num>0:
                positive_num.append(num)
            else:
                negative_num.append(num)
        
        i,j = 0,0
        while j<len(nums)//2:
            output.append(positive_num[i])
            i+=1
            output.append(negative_num[j])
            j+=1
        return output
    
sol = Solution()
print(sol.rearrangeArray([-2,2]))