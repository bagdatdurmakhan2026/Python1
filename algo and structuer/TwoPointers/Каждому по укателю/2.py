class Solution:
    def res(self, nums, nums2):
        nums.sort()
        nums2.sort()
        l = 0
        r = len(nums)
        l2 = 0
        r2 = len(nums2)
        arr = []
        while (l < r and l2 < r2):
            if nums[l] <= nums2[l2]:
                arr.append(nums[l])
                l += 1  
            else :
                arr.append(nums2[l2])
                l2 += 1
        while l < r:
            arr.append(nums[l])
            l += 1
        while l2 < r2:
            arr.append(nums2[l2])
            l2 += 1
        return arr

nums = [1,2,5,7]
nums2 = [5,4,5,8]
print(Solution().res(nums, nums2)) ## [1, 2, 4, 5, 5, 7, 8]
"""
дан массив nums = [1,3,5,7] и nums2 = [2,4,6,8], нужно обьединить их в 2 массива с помощью двух указателей.
пример если длини одного массива меньше другого, то нужно использовать максимальную длину массива для условия while. В данном случае, так как массивы не имеют общих элементов, результат будет пустым массивом.
например 1 меньше 2 сначала закидываем 1 элемент потом 2 так как я отсортивал массивы
                l2 += 1
        return arr

nums = [1,2,5,7]
nums2 = [5,4,5,8]
print(Solution().res(nums, nums2))
"""         