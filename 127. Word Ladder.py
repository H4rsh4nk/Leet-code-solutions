class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int answer = *max_element(nums.begin(), nums.end());
        int max_v=1, min_v=1,temp;
        for( int i = 0; i < nums.size(); i++){
            if (nums[i] == 0){
                min_v = 1;
                max_v = 1;
                continue;
            }
            temp  = nums[i]*max_v;
            max_v = max(max(nums[i]*min_v, nums[i]*max_v), nums[i]);
            min_v = min(min(nums[i]*min_v, temp), nums[i]);
            answer = max(answer, max_v);
        }
        cout << answer;
        return answer;
    }
};