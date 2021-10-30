


def quickSort(arr,left,right):
    index = partition(arr,left,right)
    if(left < index -1):
        quickSort(arr,left,index-1)

    if(index<right):
        quickSort(arr,index,right)




def partition(arr,left,right):

    pivot = int((left+right)/2.0)
    value= arr[pivot]
    while(left<=right):

        while(arr[left]<value):
            left+=1
        
        while(arr[right]>value):
            right-=1

        if(left <= right):
            swap(arr,left,right)
            left+=1
            right-=1
    return left



def swap(arr,i,j):

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


if __name__=="__main__":
    arr = [1,3,8,12,21,4,2,0]
    print(quickSort(arr,0,len(arr)-1))
    print(arr)