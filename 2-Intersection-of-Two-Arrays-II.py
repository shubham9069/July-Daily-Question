# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=daily-question&envId=2024-07-02

class Solution(object):
    def intersect(self, nums1, nums2):
        mp = {}
        arr = []
        for elem in nums1:
            mp[elem] = mp.get(elem,0)+1
        
        for elem in nums2:
            if elem in mp:
                arr.append(elem)
                mp[elem] -=1
                if mp[elem] == 0:
                    del mp[elem] 
            
        return arr

        