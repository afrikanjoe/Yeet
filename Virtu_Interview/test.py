import copy

def final_scores(inp):
    temp = inp 
    while True:
        current = [temp[0]]
        for i in range(1,len(temp)-1):
            student = temp[i]
            if(student<temp[i-1] and student<temp[i+1]):
                current.append(student+1)
            elif(student>temp[i-1] and student>temp[i+1]):
                current.append(student-1)
            else:
                current.append(student)
        current.append(temp[-1])
        print(current)
        if(current==temp):
            break
        else:
            temp = current
    return current




if __name__=="__main__":
    test1 = [1,6,3,4,3,5]
    test2 = [100,50,40,30]
    final_scores(test1)
    final_scores(test2)