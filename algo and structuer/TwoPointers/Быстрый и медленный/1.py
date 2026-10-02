## [0,1,0,0,3,12,2]
## output : [0,0,0,1,3,12,2]
class Solution(object):
    def res(self, nums):
        slow = 0
        fast = 0
        r = len(nums)-1
        arr = []
        while fast <= r:
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            else: fast += 1
        return nums
nums = [0,1,0,0,3,12,2]
print(Solution().res(nums))
            
#если элемент не нулевой, то мы его меняем местами с элементом на позиции медленного указателя и увеличиваем медленный указатель. 
# Если элемент нулевой, то мы просто увеличиваем быстрый указатель. 
# В конце мы получаем массив с нулями в начале и ненулевыми элементами в конце.
#
#
#
    
        