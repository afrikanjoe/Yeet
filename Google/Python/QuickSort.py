def quickSort(arr,left,right):
    # this will return the index of where things are in their proper order
    index = partition(arr,left,right)

    # call quick sort on subarrays the if statements are base cases
    if(left < index -1):
        quickSort(arr,left,index-1)

    if(index<right):
        quickSort(arr,index,right)


def partition(arr,left,right):
    print(left)
    pivot = int((left+right)/2.0)
    print("pivot",pivot)
    value= arr[pivot]

    while(left<=right):
        
        # find first left item that's out of place
        while(arr[left]<value):
            left+=1
        
        # find first right value that's out of place
        while(arr[right]>value):
            right-=1

        # if they are different swap them 
        # and increment the counters appropriately
        if(left <= right):
            swap(arr,left,right)
            left+=1
            right-=1
    
    # the pivot may get moved so you return the index of where items are in correct order before
    return left

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


if __name__=="__main__":
    arr = [1,3,8,12,21,4,2,0]
    print(quickSort(arr,0,len(arr)-1))
    print(arr)