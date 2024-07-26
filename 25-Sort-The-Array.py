# https://leetcode.com/problems/sort-an-array/?envType=daily-question&envId=2024-07-25

class Solution(object):
    def sortArray(self, nums):
        def merge(low,mid,high):
            arr = []
            i=low
            j = mid+1
            while i<=mid and j<=high:
                if nums[i] <= nums[j]:
                    arr.append(nums[i])
                    i+=1
                else:
                    arr.append(nums[j])
                    j+=1
            while i<=mid:
                arr.append(nums[i])
                i+=1
            while j<=high:
                arr.append(nums[j])
                j+=1
            for i in range(low,high+1):
                nums[i] = arr[i-low]

        def merge_sort(low, high):
            if low >= high:
                return
            mid =(low+high) // 2
            merge_sort(low, mid)
            merge_sort(mid+1, high)
            merge(low,mid,high)

        merge_sort(0, len(nums) - 1)
        return nums