class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l<=r:
            
            m = (l+r)//2
            # print(l, r, m)
            # print(nums[l], nums[r], nums[m])
            if nums[m] == target or nums[r] == target or nums[l] == target:
                return True

            if nums[l] < nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[l] > nums[m]:
                if target >= nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            else:
                l+= 1

        return False
            

        
        