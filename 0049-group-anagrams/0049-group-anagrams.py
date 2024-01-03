class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #기본적으로 빈 리스트를 값으로 가지는 딕셔너리
        anagrams = collections.defaultdict(list) 
        
        #str 리스트 요소에 대해 반복
        #키값 단어를 정렬, 해당 단어를 키로 하여 word를 추가함
        for word in strs:
            anagrams[' '.join(sorted(word))].append(word)

        return anagrams.values()