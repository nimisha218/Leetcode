class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""

        i = 0

        while True:
           
            if len(strs[0]) <= i:
               
                return result
            check = strs[0][i]

            for j in range(1, len(strs)):

                if len(strs[j]) <= i or check != strs[j][i]:
                   
                    return result
            
            result += check
            i += 1
        
