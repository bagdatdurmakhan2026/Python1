class Solution:
    def res(self, nums, nums2):
        l = 0
        r = len(nums)-1
        l2 = 0
        r2 = len(nums2)-1
        arr = []
        while l <= r and l2 <= r2:
            if nums[l] == nums2[l2]:
                arr.append(nums[l])
                l += 1
                l2 += 1
            elif nums[l] < nums2[l2]:
                l += 1
            else:
                l2 += 1
        return arr

nums = [1,2,3,4,5]
nums2 = [3,4,5,6,7]
print(Solution().res(nums, nums2))
                
        