class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        f= len(matrix[0])
        l = 0
        r = (n*f)-1
        while l<=r:
            mid = (l+r)//2
            val = matrix[mid//f][mid%f]
            if val==target:
                return True
            elif val < target:
                l = mid+1
            else:
                r = mid-1
        return False
"""[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
     """
# method ravel() only in numpys system
"""2D [R, C]	
r = mid // C


c = mid % C
3D [D, R, C]	
d = mid // (R * C)


r = (mid % (R * C)) // C


c = mid % C
4D [H, D, R, C]	
h = mid // (D * R * C)


d = (mid % (D * R * C)) // (R * C)


r = (mid % (R * C)) // C


c = mid % C
        """