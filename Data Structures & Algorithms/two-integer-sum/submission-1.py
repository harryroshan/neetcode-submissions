class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {}
        for i in range(0, len(nums)):
            if nums[i] not in nums_hashmap:
                nums_hashmap[nums[i]] = [i]
            else:
                nums_hashmap[nums[i]].append(i)
        for i in range(0, len(nums)):
            rem_num = target - nums[i]
            if rem_num in nums_hashmap:
                if rem_num != nums[i]:
                    return [i, nums_hashmap[rem_num][0]]
                elif len(nums_hashmap[rem_num]) > 1:
                    return [nums_hashmap[rem_num][0], nums_hashmap[rem_num][1]]