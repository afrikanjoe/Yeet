




def pairs(arr,k):
    arr = sorted(arr)
    p1 = 0 
    p2 = 1
    output = []
    while p1<p2 and p2<len(arr):
        val1 = arr[p1]
        val2 = arr[p2]
        if(abs(val1-val2)==k):
            output.append((val1,val2))
            p2+=1
        elif(abs(val1-val2)<k):
            p2+=1
        else:
            p1+=1
    return output

if __name__ == "__main__":
    inp1 = [1,7,5,9,12,3]
    print(pairs(inp1,2))
