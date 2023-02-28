class Solution {
    public int maxArea(int[] height) {
        
        int left = 0;
        int right = height.length - 1;
        
        int max = 0;
        
        int area = 0;
        
        while(left < right){
            
            if (height[left] < height[right]){
                area = (right - left) * height[left];
                left = left + 1;
            }
            else if(height[right] < height[left]){
                area = (right - left) * height[right];
                right = right - 1;
            }
            else{
                area = (right - left) * height[left];
                left = left + 1;
                right = right - 1;
            }
            
            if (area > max){
                max = area;
            }
        }
        
        return max;
    }
}