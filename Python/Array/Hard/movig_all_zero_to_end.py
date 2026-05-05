def move_zero(arr):
    start=0
    end=1
    while end<len(arr):
        if arr[start]==0:
            arr[start],arr[end]=arr[end],arr[start]
            start +=1
            end +=1
    return arr

arr=[1,4,0,8,0,6,3]
move_zero(arr)

print(arr)