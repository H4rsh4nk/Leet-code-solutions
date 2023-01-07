class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        int temp = 0, len = nums.size();
        for(int i = 0; i < len; i++){
            if(nums[i - temp] != val){
                count++;
            }else{
                nums.erase(nums.begin() + i - temp);
                temp++;
            }
        }
        return count;

    }
};