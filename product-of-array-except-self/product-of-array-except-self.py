class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = []
        post = []

        for i in nums:
            if len(pre) < 1:
                pre.append(i)
                continue
            pre.append(i*pre[-1])
        for i in nums[::-1]:
            if len(post) < 1:
                post.insert(0, i)
                continue

            post.insert(0, i * post[0])
        ret = []
        for i in range(len(nums)):
            if i == 0:
                ret.append(post[1])
                continue
            if i == len(nums)-1:
                ret.append(pre[-2])
                continue

            ret.append(pre[i-1]*post[i+1])

        return ret