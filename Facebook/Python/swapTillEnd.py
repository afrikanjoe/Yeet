
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 

def swaptilend(arr,num):

    left = 0 
    right = len(arr)-1 
    while left<right:
        val1 = arr[left]
        val2 = arr[right]
        if(val2==num):
            right=right-1
        elif(val1==num):
            swap(arr,left,right)
        else:
            left+=1
    return num 

if __name__ == "__main__":
    arr = [9,7,8,9,1,2,3,3,4,6,7,2,9]
    swaptilend(arr,1)
    print(arr)

    arr = [1,2,3,3,4,6,7,2,9]
    swaptilend(arr,6)
    print(arr)

    arr = [1,2,3,3,4,6,7,2,9]
    swaptilend(arr,3)
    print(arr)

    arr = [9,7,8,9,1,2,3,3,4,6,7,2,9]
    swaptilend(arr,9)
    print(arr)
