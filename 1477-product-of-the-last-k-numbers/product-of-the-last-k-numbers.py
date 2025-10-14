class ProductOfNumbers:

    def __init__(self):
        self.products = []
        self.product = 1

    def add(self, num: int) -> None:
        ## handle 0
        if num:
            self.product *= num
            self.products.append(self.product)
        else:
            self.product = 1
            self.products = []
        
    def getProduct(self, k: int) -> int:
        if k > len(self.products):
            return 0
        if k == len(self.products):
            return self.products[-1]
        else:
            return int(self.products[-1] / self.products[-1 - k])


        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)