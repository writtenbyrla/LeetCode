class MyQueue:
    #queue: FIFO 선입선출
    
    def __init__(self):
        self.input = []
        self.output = []

    # 큐의 마지막에 x 삽입    
    def push(self, x: int) -> None:
        self.input.append(x)

    # 큐의 처음에 있는 요소 삭제
    # 
    def pop(self) -> int:
        self.peek() #뒤집은 요소
        return self.output.pop() #스택은 오른쪽에서부터 제거
        
    # 큐의 처음에 있는 요소 조회
    def peek(self) -> int:
        if not self.output: #output 배열에 요소가 존재하지 않으면
            while self.input: #input 리스트에 남는게 없을 때 까지
                self.output.append(self.input.pop())
        return self.output[-1] #-1은 가장 끝에 있는 요소   
            
        
    # 큐가 비었는지 확인
    def empty(self) -> bool:
        return (len(self.input)==0) and (len(self.output)==0)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()