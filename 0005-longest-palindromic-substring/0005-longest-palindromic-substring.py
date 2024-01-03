class Solution:
    def longestPalindrome(self, s: str) -> str:
#한 글자일 경우, s를 뒤집었을 때 s와 같은 경우 s 그대로 반환
        if len(s) ==1 or s == s[::-1]: return s
        
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]



	# 문자열 길이가 가장 큰 값 result에 담아서 반환
        result = ''
        for i in range(len(s) - 1):
		#for문 돌리면서 현재 가장 문자열이 긴 단어 result에 담아서 함께 비교
            result = max(result, 
            		# 짝수인 경우 한 자리씩 비교
                         expand(i, i + 1), 
                         # 홀수인 경우 두 자리씩 비교
                         expand(i, i + 2),
                         key=len)
        return result