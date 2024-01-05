class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return len(s)

        # 현재 구간의 위치 인덱스를 담는 테이블
        char_list = {}

        max_len = 0 # 문자열 길이
        start = 0  # 시작 지점

        for index, char in enumerate(s):  # 인덱스를 붙여 for문 돌림

            # char_list에 담긴 문자일 경우 start 위치를 다음으로 옮김
            if char in char_list and start <= char_list[char]:
                start = char_list[char] + 1

            # char_list에 담긴 문자가 아닌 경우(아직 겹친 문자가 없음)
            # 최대 길이
            # 를 구하기 위해 max_len값을 올림
            else:
                # 현재 max_len와 새로 구한 문자열 길이 중 큰 값을 max_len으로 함
                max_len = max(max_len, index - start + 1)

            # 현재 문자의 인덱스를 char_list에 담음
            char_list[char] = index

        return max_len