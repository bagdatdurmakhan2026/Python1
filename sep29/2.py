class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = set()
        n = len(nums)
        
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
                        
        return [list(t) for t in res]
'''
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # Если число больше 0, то сумма трех положительных чисел никогда не будет равна 0
            if nums[i] > 0:
                break
                
            # Пропускаем дубликаты первого элемента
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Пропускаем дубликаты для left и right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1   # Нужна большая сумма -> сдвигаем влево
                else:
                    right -= 1  # Нужна меньшая сумма -> сдвигаем вправо
                    
        return res
'''
