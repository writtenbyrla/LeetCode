class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        count = collections.defaultdict(int)
        answer = 0
        
        for char in stones:
            count[char] += 1
            
        for char in jewels:
            if char in count:
                answer += count[char]
        
        return answer