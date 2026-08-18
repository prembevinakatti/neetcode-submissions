class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)) :
            comple = target - nums[i]

            if comple in hashmap :
                return [hashmap[comple],i]

            hashmap[nums[i]] = i