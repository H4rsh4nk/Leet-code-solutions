class Solution {
public:
vector<vector<int>> MyfloodFill(vector<vector<int>>& image, int sr, int sc, int color, int temp) {
    if(image[sr][sc] == color || sr < 0 || sc < 0 || sr > image.size() || sc > image[0].size()) return image;

    image[sr][sc] = color;
    
    if( sr + 1 < image.size()){
        if(image[sr+1][sc] == temp){
            MyfloodFill(image,sr+1,sc,color,temp);
        }
    }
    if(sc + 1 < image[0].size()){
        if(image[sr][sc+1] == temp){
            MyfloodFill(image,sr,sc+1,color,temp);
        }
    }

    if(sc -1 >= 0){    
        if(image[sr][sc-1] == temp){
            MyfloodFill(image,sr,sc-1,color,temp);
        }}
    if(sr - 1 >= 0){
        if(image[sr-1][sc] == temp){
            MyfloodFill(image,sr-1,sc,color,temp);
    }}

    return image;
        
}
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
       int temp = image[sr][sc];
        if(image[sr][sc] == color || sr < 0 || sc < 0 || sr > image.size() || sc > image[0].size()   ) return image;

        return MyfloodFill(image, sr, sc, color, temp);    

        
        // return image;
    }
};