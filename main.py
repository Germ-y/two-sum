from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_dict={}
    for i,num in enumerate(nums):
        sub=target-num
        if sub in num_dict:
            return [num_dict[sub], i]
        num_dict[num]= i

# print(twoSum([2,7,11,15],9))
# print(twoSum([3,2,4],6))
# print(twoSum([3,3],6))
