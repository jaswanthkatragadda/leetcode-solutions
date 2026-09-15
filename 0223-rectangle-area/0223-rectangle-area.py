class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        width = min(ax2,bx2) - max(ax1,bx1)
        length = min(ay2,by2) - max(ay1,by1)

        if width < 0 :
            width = 0 
        if length < 0 :
            length = 0 

        O_area = width*length

        Rect1_area = (ax2 - ax1) * (ay2 - ay1)
        Rect2_area = (bx2 - bx1) * (by2 - by1)

        Total_area = (Rect1_area + Rect2_area) - O_area
        
        return Total_area