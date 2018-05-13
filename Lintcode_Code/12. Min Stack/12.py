class MinStack:

    def __init__(self):
        """
        @param: number: An integer
        @return: nothing
        """
        self.stack = []
        self.minstack = []

    def push(self, number):
        """
        @return: An integer
        """
        self.stack.append(number)
        if not self.minstack or number <= self.minstack[-1]:
            self.minstack.append(number)

    def pop(self):
        """
        @return: An integer
        """
        if self.minstack[-1] == self.stack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    def min(self):
        return self.minstack[-1]
