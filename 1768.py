class solution:
    def mergeAlternately (self, word1:str, word2:str)-> str:
        merged_string = ""
        len1 = len(word1)
        len2 = len(word2)

        for i in range(max(len1,len2)):
            if i < len1:
                merged_string+= word1[i]
            if i < len2:
                merged_string+= word2[i]

        return merged_string
    

sol = solution()
print(sol.mergeAlternately('ab','pqrs'))