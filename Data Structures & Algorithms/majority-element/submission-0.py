class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        count = 0

        for num in nums :
            if count == 0:
                cand = num

            if num == cand :
                count += 1
            else:
                count -= 1
        
        return cand