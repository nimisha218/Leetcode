class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        # Convert the word string to a word list
        word = list(word)

        left = 0
        flag = 0

        # To find right, find the ch character in the list
        for i in range(len(word)):
            right = i
            if word[i] == ch:
                flag = 1
                break
        
        if flag == 0:
            return "".join(word)

        while left <= right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        
        return "".join(word)