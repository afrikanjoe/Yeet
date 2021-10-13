"""
One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. 
Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.
For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 
3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). 
Note that the non-alphanumeric characters remain unchanged.
Given a string and a rotation factor, return an encrypted string.
Signature
string rotationalCipher(string input, int rotationFactor)
Input
1 <= |input| <= 1,000,000
0 <= rotationFactor <= 1,000,000
"""

class Solution:
    def __init__(self):
        pass
    def rotationalCipher(self,input, rotation_factor):
        # Write your code here
        output = ''
        for i in input:
            if(i.isnumeric()):
                output = output + str((int(i) + rotation_factor) % 10)
            else:
                upper = i.isupper()
            if(upper):
                i = i.lower()
            if(ord(i)<97 or ord(i)>122):
                output = output + i
                continue
            i_ord = ord(i) - 97 + rotation_factor
            i_ord = (i_ord % 26) + 97
            if(upper):
                output = output + chr(i_ord).upper()
            else:
                output = output + chr(i_ord)
            
        return output 


if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = Solution().rotationalCipher(input_1, rotation_factor_1)
  print(output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = Solution().rotationalCipher(input_2, rotation_factor_2)
  print(output_2)