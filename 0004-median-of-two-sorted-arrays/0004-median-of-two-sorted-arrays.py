class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1
        B = nums2

        total = len(A) + len(B)
        half = total // 2

        # Force A to be < B
        if len(A) > len(B):
            A, B = B, A

        # Initialize left and right pointers for A
        left = 0
        right = len(A) - 1

        while True:

            a_mid = (left + right) // 2

            b_mid = half - a_mid - 2 # -1 to offset the indexes

            a_left = A[a_mid] if a_mid >= 0 else float("-infinity")
            a_right = A[a_mid + 1] if (a_mid + 1) < len(A) else float("infinity")
            b_left = B[b_mid] if b_mid >= 0 else float("-infinity")
            b_right = B[b_mid + 1] if (b_mid + 1) < len(B) else float("infinity")

            # Right partition found
            if a_left <= b_right and b_left <= a_right:
                # Odd
                if total % 2:
                    return min(a_right, b_right)
                #Even
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2

            elif a_left > b_right:
                right = a_mid - 1
            
            else:
                left = a_mid + 1

            

        
        