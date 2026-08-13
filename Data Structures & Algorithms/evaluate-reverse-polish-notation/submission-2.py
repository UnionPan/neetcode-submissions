class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        operators = []
        for token in tokens:
            if token not in ops:
                operands.append(int(token))
            else:
                num2 = operands.pop()
                num1 = operands.pop()
                new_num = ops[token](num1, num2)
                operands.append(new_num)

        return operands[-1]
                
