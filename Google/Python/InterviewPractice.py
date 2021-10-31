

def mergeANB(arr1,arr2):
    res = []
    while arr1 and arr2:
        val1 = arr1[0]
        val2 = arr2[0]

        if(val1<=val2):
            res.append(arr1.pop(0))
        else:
            res.append(arr2.pop(0))

    if(arr1):
        for i in arr1:
            res.append(i)
    if(arr2):
        for i in arr2:
            res.append(i)
    return res


def mergeInPlace(A,B):
    start = len(A)
    A = A + [0]*len(B)
    for i in B: 
        A[start] = i
        swap = start
        while swap-1>=0 and A[swap-1]>A[swap]:
            swapArr(A,swap-1,swap)
            swap-=1
        start+=1
    return A

def swapArr(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp 


if __name__ == "__main__":
    A = [1,2,3,4,5]
    B = [10,11,12,14,15]
    print(mergeInPlace(A,B))

    A = [2,4,6,8,10]
    B = [1,3,5,7,9]
    print(mergeInPlace(A,B))

    A = [1,2,3,4,5]
    B = [10,11,12,14,15]
    print(mergeANB(A,B))

    A = [2,4,6,8,10]
    B = [1,3,5,7,9]
    print(mergeANB(A,B))