class Solution(object):
    def searchMatrix(self, matrix, target):
        c = [a for b in matrix for a in b]
        if target in c:
            return True
        return False
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """     
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# time is  O(mxn)