from typing import List
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.c1 = Counter(nums1)
        self.c2 = Counter(nums2)

        self.nums1 = nums1
        self.nums2 = nums2


    def add(self, index: int, val: int) -> None:
        t = self.nums2[index]
        self.c2[t] -= 1
        self.c2[t+val] += 1
        self.nums2[index] = t + val


    def count(self, tot: int) -> int:
        s = 0
        for k, v in self.c1.items():
            s += self.c2[tot - k] * v
        return s


nums1, nums2 = [1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]
# Your FindSumPairs object will be instantiated and called as such:
obj = FindSumPairs(nums1, nums2)

print('count 7')
print(obj.count(7))

index, val = 3, 2
obj.add(index,val)

tot = 8
print('count {}'.format(tot))
print(obj.count(tot))


tot = 4
print('count {}'.format(tot))
print(obj.count(tot))

index, val = 0, 1
obj.add(index,val)

index, val = 1, 1
obj.add(index,val)

tot = 7
print('count {}'.format(tot))
print(obj.count(tot))


[1,2,3,4]
print(hash('123'))









