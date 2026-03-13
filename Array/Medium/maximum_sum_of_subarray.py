# Write a Python program to find the maximum sum of any subarray of size k.




def max_sum_subarray(arr,k):
    i,j,sub_arr = 0,k,[]
    while j<=len(arr):
        sub_arr.append(sum(arr[i:j]))
        i+=1
        j+=1
    return max(sub_arr)
    
   
arr = [2,1,5,1,3,2]
print(max_sum_subarray(arr,3))

