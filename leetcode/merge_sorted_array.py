class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        # tira os 0s da jogada
        for i in range(n):
            nums1.pop()
        
        for i in nums2:
            current_index = 0
            while i > nums1[current_index]:
                current_index += 1
                if current_index == len(nums1):
                    break
            nums1.insert(current_index, i)

        print(nums1)

solution = Solution()
solution.merge(nums1 = [1,2,3,8,0,0,0], m = 4, nums2 = [2,5,6], n = 3)