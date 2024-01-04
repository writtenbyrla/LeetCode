class Solution:
    def isValid(self, s: str) -> bool:

    # 괄호 짝 dict로 만들기(key-value)
        pair = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        stack = []

        opener = "({["

        for item in s:
            # opener는 stack에 넣기
            if item in opener:
                stack.append(item)

            # opener가 아닌 경우
            else:   
                # stack이 비어있으면(맞는 짝이 없다는 이야기)
                if not stack: 
                    return False

                # stack이 비어있지 않으면 가장 뒤에 있는 opener 꺼내서
                top = stack.pop()
                # 방금 꺼낸 것과 짝이 맞는지 확인 후 다를 경우 false
                if pair[item] != top:
                    return False

        return not stack       