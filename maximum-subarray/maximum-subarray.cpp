#include <vector>
#include <iostream>
#include <math.h>

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = nums[0];
        int curr = 0;

        for(int i: nums){
            if(curr < 0){
                curr = 0;
            }
            curr += i;
            sum = max(sum, curr);
        }

        return sum;
    }
};