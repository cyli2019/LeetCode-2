#!python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # python dict, 
        for idx, item in enumerate(nums):
            want = target - item
            if want in hashmap: # o(1) for python dict in operation
                return [hashmap[want],idx]
            hashmap[item] = idx # keys are unique
        


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert (Solution().twoSum(nums, target) == [0, 1])
    nums = [3, 2, 4]
    target = 6
    assert (Solution().twoSum(nums, target) == [1, 2])
