class Solution:
    def longestPalindrome(self, s: str) -> str:
        #한 글자일 경우, s를 뒤집었을 때 s와 같은 경우 s 그대로 반환
        if len(s) == 1 or s == s[::-1]: return s

        #팰린드롬 담을 리스트 선언
        p_list = []

        for i in range(len(s)):
            for j in range(len(s), i, -1):
                #i~j까지 문자열과 뒤집었을때 문자열 비교하여 일치하면 빈 리스트에 담음
                if s[i:j] == s[i:j][::-1]:
                    p_list.append(s[i:j])

        return max(p_list, key=len)
