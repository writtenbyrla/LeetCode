import bisect
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, x in enumerate(numbers, start=1):
            y = target-x
            y_idx = bisect.bisect_left(numbers, y, lo=idx)

            if y_idx < len(numbers) and numbers[y_idx] == y:
                return [idx, y_idx+1]