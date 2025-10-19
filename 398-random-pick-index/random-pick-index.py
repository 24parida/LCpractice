class Solution:

    def __init__(self, nums: List[int]):
        self.num_to_idx = collections.defaultdict(list)
        for x, num in enumerate(nums):
            self.num_to_idx[num].append(x)

    def pick(self, target: int) -> int:
        return random.choice(self.num_to_idx[target])

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)