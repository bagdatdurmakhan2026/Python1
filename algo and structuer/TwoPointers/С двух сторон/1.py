class Solution(object):
    def sum(self, nums, target):
        l = 0 
        r = len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                return [l, r]
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l+=1
        return []
nums = [3,2,4]
target = 6
print(Solution().sum(nums, target))
# Метод двух указателей (Two Pointers) используется для поиска двух чисел в отсортированном массиве, которые в сумме дают заданное значение (target). никак иначе на примере nums = [3,2,4]
#target = 6
#тут нужно другое решение, так как массив не отсортирован. В данном случае можно использовать хэш-таблицу (словарь) для хранения индексов элементов и их значений. Вот пример решения: