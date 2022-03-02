class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {index:target - num2 for index, num2 in zip(range(len(nums)), nums)}

        for index, required in dictionary.items():
            try:
                output = [index, nums.index(required)]
                if output[0] == output[1]:
                    assert balls
            except:
                pass
            else:
                return output
