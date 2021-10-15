

def findEncryptedWord(s):
  # Write your code here
  s_em = ""
  # base case
  if(len(s)<=1):
    return s
  else:
    low = 0
    high = len(s)-1
    mid = int((low+high)/2)
    print(s,mid)
    s_em = s_em + s[mid]
    s_em = s_em+findEncryptedWord(s[0:mid]) 
    s_em = s_em+findEncryptedWord(s[mid+1:])
    return s_em


if __name__=="__main__":
  s1 = "abc"
  expected_1 = "bac"
  output_1 = findEncryptedWord(s1)
  print(output_1)

  s2 = "abcd"
  expected_2 = "bacd"
  output_2 = findEncryptedWord(s2)
  print(output_2)