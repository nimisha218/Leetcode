class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        def binary_search(potions, target):

            # We want to return the left pointer (insertion) from this method
            # Don't return potions[mid] == target, because we don't want a match. We want the left pointer.

            left = 0
            right = len(potions) - 1

            while left <= right:

                mid = (left + right) // 2
                
                if potions[mid] < target:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
            return left

        # Sort the potions array
        potions.sort()

        m = len(potions)

        ans = []
        
        for spell in spells:
            target = success / spell
            index = binary_search(potions, target)
            ans.append(m - index)

        return ans
        