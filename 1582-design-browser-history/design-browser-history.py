class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = homepage
        self.fstack = []
        self.bstack = []

    def visit(self, url: str) -> None:
        self.fstack.append(self.cur)
        self.cur = url
        self.bstack = []

    def back(self, steps: int) -> str:
        while self.fstack and steps > 0:
            self.bstack.append(self.cur)
            self.cur = self.fstack.pop()
            steps -=1
        return self.cur

    def forward(self, steps: int) -> str:
        while self.bstack and steps > 0:
            self.fstack.append(self.cur)
            self.cur = self.bstack.pop()
            steps -= 1
        return self.cur


        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)