class Solution:
    def reverseWords(self, s: str) -> str:

        s_list = []

        for word in s:
            s_list.append(word)
        
        s_list = s_list[-1::-1]

        s = "".join(s_list)
        
        s_list = s.split(" ")

        s = s_list[-1::-1]

        return " ".join(s)
        
        

        