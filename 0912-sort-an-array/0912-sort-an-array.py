class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 병합 정렬 이용하여 풀이
        def merge(arr1, arr2):
            result = []
            i = j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1

            while i < len(arr1):
                result.append(arr1[i])
                i += 1

            while j < len(arr2):
                result.append(arr2[j])
                j += 1

            return result

        def mergesort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]

            return merge(mergesort(L), mergesort(R))

        return mergesort(nums)