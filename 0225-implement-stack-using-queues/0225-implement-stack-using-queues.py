class MyStack:

    def __init__(self):
        # stack은 오른쪽만 사용 가능한데, 
        # 양방향으로 요소를 조작해야 하므로 deque를 이용하여 스택 구현
        self.q = collections.deque() 
        
    # 스택의 첫 번째에 x 삽입
    # 원래 스택은 요소 삽입시 가장 오른쪽으로 가므로
    # 삽입 후 왼쪽으로 가도록 정렬해주어야 함
    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    # 첫 번째 요소 삭제
    # 가장 왼쪽에 있는 요소 삭제 
    def pop(self) -> int:
        return self.q.popleft()
        
    # 첫 번째 요소 반환
    def top(self) -> int:
        return self.q[0]
        
    # 스택이 비어있는지 확인
    def empty(self) -> bool:
        return len(self.q)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()