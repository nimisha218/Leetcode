class Solution:
    def reverseWords(self, s: str) -> str:

        # Convert the string into a list
        s_list = []
        for ch in s:
            s_list.append(ch)
        
        # Reverse the list
        s_list = s_list[::-1]

        # Convert it to a string again
        result = "".join(s_list)

        result = result.split(" ")

        result = result[::-1]

        result = " ".join(result)

        return result

        