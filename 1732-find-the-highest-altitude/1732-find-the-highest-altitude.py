class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        # Compute the prefix array
        prefix = [gain[0]]

        for i in range(1, len(gain)):
            prefix.append(prefix[-1] + gain[i])
        
        return max(prefix) if max(prefix) >= 0 else 0