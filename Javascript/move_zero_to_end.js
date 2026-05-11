function move_zero_to_end(arr) {
    //firrst loop which start from 0 to end of array
    for(let i=0;i<arr.length;i++){
        //second loop which start from i+1 to end of array
        for(let j=i+1;j<arr.length;j++){
            //if the current element is 0 then swap it with the next element
            if(arr[i]===0){
                let temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
            }
        }
    }
    //returning the modified array
    return arr
}

let arr=[4,2,4,0,0,3,0,5,1,0]


console.log(move_zero_to_end(arr));
