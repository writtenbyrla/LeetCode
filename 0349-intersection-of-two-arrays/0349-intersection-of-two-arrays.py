from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if not nums1 or not nums2:
            return []
        
        result = set()
        nums2.sort()
        
        for n1 in nums1:
            # nums1 요소 하나씩 nums2에 있는지 확인하여 인덱스 반환
            idx = bisect.bisect_left(nums2, n1)
            if len(nums2) > idx and n1 == nums2[idx]:
                result.add(n1)

        return list(result)