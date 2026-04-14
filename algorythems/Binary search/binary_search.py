

def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid= (low+high)//2
        if target==arr[mid]:
            return mid
        
        if target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
    

arr=[3,6,8,12,14,17,25,29,31,36,42,47,53,55]
target=25

print(binary_search(arr,target))