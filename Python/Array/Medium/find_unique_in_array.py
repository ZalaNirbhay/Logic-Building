def find_unique(nums):
    uniques=[]
    for num in nums:
        if num not in uniques:
            uniques.append(num)
        
    return len(uniques)

# nums=[1, 2, 2, 3, 4, 4, 6, 6, 5]
nums=[1,1,1,1,1,1]
print(find_unique(nums))