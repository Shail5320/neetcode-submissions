class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ptr = -1
        for i in range(len(operations)):
            if operations[i] == 'C':
                stack.pop()
                ptr-=1
            elif operations[i] == 'D':
                stack.append(2*int(stack[ptr]))
                ptr+=1
            elif operations[i] == '+':
                stack.append(int(stack[ptr]) + int(stack[ptr-1]))
                ptr+=1
            else:
                stack.append(operations[i])
                ptr+=1
        
        s = 0
        for i in stack:
            s+=int(i)
        return s