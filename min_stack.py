# Problem url: https://leetcode.com/problems/min-stack


class MinStack:

    def __init__(self):
        self._stack = []
        self._min_values = []
        self._top_values = []

    def push(self, val: int) -> None:
        if len(self._min_values) == 0 or self._min_values[-1] >= val:
            self._min_values.append(val)
        elif val <= self._stack[-1]:
            self._stack.insert(-1, val)

        if len(self._top_values) == 0 or self._top_values[-1] <= val:
            self._top_values.append(val)
        elif val >= self._stack[-1]:
            self._top_values.insert(-1, val)

        self._stack.append(val)

    def pop(self) -> None:
        if len(self._stack) == 0:
            return

        value = self._stack.pop(-1)
        if len(self._min_values) > 0 and value == self._min_values[-1]:
            self._min_values.pop(-1)

        if len(self._top_values) > 0 and value == self._top_values[-1]:
            self._top_values.pop(-1)

    def top(self) -> int:
        return self._top_values[-1]

    def getMin(self) -> int:
        return self._min_values[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    minStack.getMin()  # return -3
    minStack.pop()
    minStack.top()  # return 0
    minStack.getMin()  # return -2
