class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        left = 0
        right = len(s) - 1

        s_list = list(s)

        while left <= right:

            if s_list[left].isalpha() and s_list[right].isalpha():
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            
            else:
                if s_list[left].isalpha():
                    right -= 1
                elif s_list[right].isalpha():
                    left += 1
                else:
                    left += 1
                    right -= 1

        return "".join(s_list)
        