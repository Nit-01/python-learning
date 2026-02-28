nums=[10,20,12,15,21]

first=nums[0]
second=nums[0]

for i in (nums):
    if i>first:
        second=first
        first=i
    if i<first and i>second:
        second=i
print(second)

