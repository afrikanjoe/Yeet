"""
Write a function that returns the number of valid and unique ids for any given set of parameters (L,K,alphabet)
Ids are valid if all of the following conditions hold
- All characters are members of a given alphabet
- All characters must exist in the id
- Same character can repeat multiple times
- Id length cannot be larger than the given length L
- Runs of a single character are less than 'K'


Example 'L = 5, K = 3' alphabet = [a,b]
valid: "ab"
valid: "aba"
invalid: "a"
invalid: "bbbba"
"""

def is_id_valid(sid,alphabet,L,K):
    if(len(sid)>L):
        return False
    counter = 0 

    char_list = []


    prev_letter = None 
    for letter in sid:
        if not letter in char_list:
            char_list.append(letter)

        if(prev_letter and letter == prev_letter):
            counter +=1
            if(counter>K):
                return False
        else:
            counter = 0 

        prev_letter = letter

    return len(char_list) == len(alphabet)

def generate_valid(L,K,alphabet):
    seed = "".join(alphabet)
    queue = [seed]
    visited = []
    count = 0 
    while queue: 
        curr_str = queue.pop(0)
        for alpha in alphabet:
            for i in range(len(curr_str)+1):
                curr_add = list(curr_str)
                if(i<len(curr_str)):
                    curr_add.insert(i,alpha)
                else:
                    curr_add = curr_add + [alpha]
                curr_add = "".join(curr_add)
                if(is_id_valid(curr_add,alphabet,L,K) and curr_add not in visited):
                    queue.append(curr_add)
                    visited.append(curr_add)
    print(visited)
if __name__ == "__main__":
    alphabet = ["a","b"]
    generate_valid(5,3,alphabet)
    print(is_id_valid("aaaa",alphabet,5,3))