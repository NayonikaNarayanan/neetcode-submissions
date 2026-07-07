class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights)-1
        max_area = 0

        while left < right:
            a = (right - left)*min(heights[left],heights[right])
            
            if a>max_area:
                max_area = a

            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1

        return max_area

        