// C++ program for different tree traversals
#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> nums1 = {6,7};
    vector<int> nums2 = {6,0,4};
    int k = 5;

    vector<int> visit_nums1(nums1.size(), 0),
            visit_nums2(nums2.size(), 0);
    vector<int> answer;

    for (int i = 0, j = k - 1; i < k; i++, j--) {
    
        vector<pair<int, int>> temp;
        
        if(i < nums1.size()){
            //if visit_nums1[i] == 1, skip
            
            if(visit_nums1[i] != 1)
                temp.push_back(make_pair(nums1[i], i));
            if(visit_nums1[nums1.size() - 1 - i] != 1)
                temp.push_back(make_pair(nums1[nums1.size() - 1 - i], nums1.size() - 1 - i));

        }
        
        if(i < nums2.size()){
            if(visit_nums2[i] != 1)
                temp.push_back(make_pair(nums2[i], i));
            if(visit_nums2[nums2.size() - 1 - i] != 1)
                temp.push_back(make_pair(nums2[nums2.size() - 1 - i], nums2.size() - 1 - i));

        }

        if(j < nums1.size()){
            if(visit_nums1[j] != 1)
                temp.push_back(make_pair(nums1[j], j));
            if(visit_nums1[nums1.size() - 1 - j] != 1)
                temp.push_back(make_pair(nums1[nums1.size() - 1 - j], nums1.size() - 1 - j));

        }

        if(j < nums2.size()){
            if(visit_nums2[j] != 1)
                temp.push_back(make_pair(nums2[j], j));
            if(visit_nums2[nums2.size() - 1 - j] != 1)
                temp.push_back(make_pair(nums2[nums2.size() - 1 - j], nums2.size() - 1 - j));

        }

        for (int i = 0; i < temp.size(); i++) {
            cout << temp[i].first << " " << temp[i].second << " " << endl;
        }

        //find max from temp.first
        int max = 0, max_index = 0, arr_number = 0;
        for (int i = 0; i < temp.size(); i++) {
            if (temp[i].first > max) {
                max = temp[i].first;
                max_index = temp[i].second;
                if(i < 2)
                    arr_number = 1;
                else
                    arr_number = 2;

            }
        }
        cout << "max: " << max << endl;
        cout << "max_index: " << max_index << endl;
        cout << "arr_number: " << arr_number << endl;
        cout << "==================================" << endl;


        if (arr_number == 1) {
            answer.push_back(nums1[max_index]);
            visit_nums1[max_index] = 1;
        } else {
            answer.push_back(nums2[max_index]);
            visit_nums2[max_index] = 1;
        }
        answer.push_back(max);
    }

        return 0;
}
