class Solution {
public:
    vector<int> answer;
    vector<int> runningSum(vector<int>& nums) {
        int temp = 0;
        for(auto i : nums){
            temp += i;
            answer.push_back(temp);
        }
        return answer;
    }
};