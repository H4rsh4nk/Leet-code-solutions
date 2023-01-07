class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int left_sum=0, right_sum = 0;
        for(auto x : nums)  
            right_sum += x;
        cout << right_sum;

        for(int i = 0; i < nums.size(); i++){
            right_sum -= nums[i];
            
            if(left_sum == right_sum)
                return i;
            
            left_sum += nums[i];
        }

        return -1;
    }
};