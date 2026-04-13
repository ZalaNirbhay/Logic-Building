# # Write a Python program to move all zeros in an array to the end while maintaining the #order of non-zero elements.

# def move_zero_end(arr):
#     i,j=0,1
#     if (arr[j]!=0 and arr[i]==0):
#         arr[i], arr[j] = arr[j], arr[i]
#         i += 1

#     while(True):
#         if (i==len(arr) or j==len(arr)):
#             return arr
#         if (arr[j]==0):
#             j += 1
#         if (arr[j] != 0):
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#             j += 1
#         if i == j:
#             j += 1
   

def move_zero_end(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    return arr

arr = [1,0,0,3,12]
print(move_zero_end(arr))
                

def removeDuplicates(nums):
    return set(nums)

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))















            
        
        
        
    