#include <math.h>
#include <iostream>

class Solution {
public:
    int minv;

    int findMin(vector<int>& nums) {
        minv = nums[0];
        if(nums.size() == 1){
            return minv;
        }

        recFindMin(nums, 0, nums.size() - 1);
        return minv;
    }

    void recFindMin(vector<int>& nums, int l, int r){
        if (l > r){
            return;
        }
        if(nums[l] < nums[r]){
            minv = min(minv, nums[l]);
            return;
        }

        int m = (l+r)/2;
        minv = min(minv, nums[m]);

        if (nums[m] >= nums[l]){
            recFindMin(nums, m+1, r);
        }
        else if(nums[m] < nums[r]){
            recFindMin(nums, l, m-1);
        }
    }
};