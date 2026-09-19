class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        x_closest = max(x1,min(xCenter,x2))
        y_closest = max(y1,min(yCenter,y2))

        d = math.sqrt((xCenter - x_closest)**2 + (yCenter - y_closest)**2)

        if d**2 <= radius**2 :
            return True
        else :
            return False