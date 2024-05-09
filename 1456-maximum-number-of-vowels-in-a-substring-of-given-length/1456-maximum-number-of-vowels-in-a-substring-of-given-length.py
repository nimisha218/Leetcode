class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = {'a', 'e', 'i', 'o', 'u'}

        # Build the first valid window
        left = 0
        right = -1
        ans = 0

        for i in range(k):
            if s[i] in vowels:
                ans += 1
            right += 1

        cur_ans = ans
        while right < len(s):

            if s[left] in vowels:
                cur_ans -= 1
            left += 1

            right += 1
            if right < len(s):
                if s[right] in vowels:
                    cur_ans += 1
            else:
                break
            
            ans = max(ans, cur_ans)

        return ans
        