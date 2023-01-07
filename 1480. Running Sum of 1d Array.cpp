class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int ans = 1;
        vector<int> as;
        int temp = 0;
        int temp_l, temp_r = 1;
        for(int i=0; i<nums.size(); i++){
           
            if(nums[i] == 0){
                temp ++;
                temp_l=ans;
            }else if(temp == 1){
                temp_r *= nums[i];
            }
            ans *= nums[i];
           
        }
        for(int i=0; i<nums.size(); i++){
            if( nums[i] == 0 && temp > 1)
                as.push_back(0);
            else if(nums[i] == 0){
                as.push_back(temp_l*temp_r);
            }
            else
                as.push_back(ans/nums[i]);
        }
        cout << temp_l << temp_r;
        return as;
    }
};