class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size())
        return false;

        map<char,char> v,k;

        for (int i = 0; i < s.size(); i++){
            // for(auto x : v){
            //     cout << x << endl;
            // }
            //print map
            
            if(v.find(t[i]) == v.end() && k.find(s[i]) == k.end()){
                v[t[i]] = s[i];
                k[s[i]] = t[i];
                // replace( s.begin(), s.end(), s[i], t[i]); 
            }else{
                if (v[t[i]] != s[i] || k[s[i]] != t[i]){
                    cout << "false" << endl;
                    return false;
                }
                // continue;
            }
        }
        return true;
        
    }
};