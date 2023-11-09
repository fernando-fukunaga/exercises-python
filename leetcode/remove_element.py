class Solution:
    def removeElement(self, nums, val: int) -> int:
        k = 0
        new_order = []
        for i in range(0,len(nums)):
            if nums[i] == val:
                nums[i] = ""
            else:
                k += 1
                new_order.append(i)
        nums = [nums[i] for i in new_order]
        return k
    
Solution().removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)