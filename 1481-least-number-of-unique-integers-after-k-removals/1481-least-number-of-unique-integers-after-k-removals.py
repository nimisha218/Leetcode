from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        counts = Counter(arr)

        ordered = sorted(counts.values(), reverse=True)

        while k:
            cur_val = ordered[-1]

            if cur_val <= k:
                k -= cur_val
                ordered.pop()
            else:
                break

        return len(ordered)