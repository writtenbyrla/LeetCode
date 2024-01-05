class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 숫자 별로 빈도 카운팅
        freqs = collections.Counter(nums)
        
        # value값이 높은 순서대로 k개 뽑아서 리스트로 만듦
        freqs_list = freqs.most_common(k)
        
        
        result = [num for num, freq in freqs_list]
        
        return result