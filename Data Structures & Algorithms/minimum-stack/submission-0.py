class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if not self._min_stack:
            self._min_stack.append(val)
        elif self._min_stack[-1] >= val:
            self._min_stack.append(val)
            

    def pop(self) -> None:
        if not self._stack:
            return None
        else:
            top = self._stack.pop()
            if top == self._min_stack[-1]:
                self._min_stack.pop()
            

    def top(self) -> int:
        return self._stack[-1] if self._stack else None

    def getMin(self) -> int:
        return self._min_stack[-1] if self._min_stack else None
