'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

def twoSum(arr,target):
    l = 0
    r = len(arr)-1
    hashSet = set()
    for i in arr:
        res = target - i
        if res in hashSet:
            return [i,res]
        hashSet.add(i)
    return False

nums = list(map(int,input().split()))
target = int(input())

if(twoSum(nums,target)):
    print(f"target {target} can be made up by {twoSum(nums,target)}")
else:
    print(f"target {target} can't be formed using any pair")

print(nums)