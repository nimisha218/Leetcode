class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A = nums1
        B = nums2

        # Force len(A) to be < len(B)
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        # Compute the left partition of A
        left = 0
        right = len(A) - 1


        while True:

            i = (left + right) // 2

            # Check if i is in bounds
            a_left = A[i] if i >= 0 else float('-infinity')
            a_right = A[i + 1] if (i + 1) < len(A) else float('infinity')

            j = half - i - 2

            # Check if j is in bounds
            b_left = B[j] if j >= 0 else float('-infinity')
            b_right = B[j + 1] if (j + 1) < len(B) else float('infinity')

            # Check if the left and right partitions are valid
            if a_left <= b_right and b_left <= a_right:
                # Compute the median
                if total % 2:
                    return min(a_right, b_right)
                return (max(a_left, b_left) + min(b_right, a_right)) / 2
            
            elif a_left > b_right:
                right = i - 1
            
            else:
                left = i + 1


            

        
        