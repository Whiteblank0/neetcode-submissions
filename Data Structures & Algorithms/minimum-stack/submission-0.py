class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.minst or self.minst[-1] >= val:
            self.minst.append(val)

    def pop(self) -> None:
        element = self.st.pop()
        if element == self.minst[-1]:
            self.minst.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minst[-1]
