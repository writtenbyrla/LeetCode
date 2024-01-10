class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
    # digits 숫자에 해당하는 문자 조합 모두 구하기
    # 2(abc) 3(def) -> 가능한 모든 2자리 조합
    # 2: [a, b, c]
    # 3: [d, e, f]
    
        combination = []

        table = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        if not digits: return []
        
        def dfs(index, current_str):

            # 탐색이 끝난 경우
            if index == len(digits):
                combination.append(current_str)
                return

            for char in table[digits[index]]:
                dfs(index + 1, current_str + char) # 1, a / 1, a+d /

        dfs(0, '')

        return combination
        
        
