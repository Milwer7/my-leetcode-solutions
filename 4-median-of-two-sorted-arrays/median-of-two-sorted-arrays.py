class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        median_index = total_length // 2
        i, j = 0, 0
        current_value, previous_value = 0, 0

        for k in range(median_index + 1):
            previous_value = current_value
            
            if i < len(nums1) and (j >= len(nums2) or nums1[i] <= nums2[j]):
                current_value = nums1[i]
                i += 1
            else:
                current_value = nums2[j]
                j += 1

        if total_length % 2 == 1:
            return float(current_value)
        else:
            return (previous_value + current_value) / 2