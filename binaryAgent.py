# Intermediate Algorithm Scripting: Binary Agents
# Return an English translated sentence of the passed binary string. The binary string will be space separated.



def binaryAgent(str):
  '''Convert a string of binary characters to the ANCII characters'''
  binary = str.split()                            # split the str apart
  binary = ''.join(binary)                        # join with no spaces
  binary_int = int(binary,2)                      # convert to binary integer
  byte_number = binary_int.bit_length() +7//8     # change to byte after adding floor division of 7//8 to get integer

  binary_array = binary_int.to_bytes(byte_number,'big') 
  ascii_text = binary_array.decode()              # decode binary converted characters
  print(ascii_text.strip())


binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111") 
# #should return "Aren't bonfires fun!?"
binaryAgent("01001001 00100000 01101100 01101111 01110110 01100101 00100000 01010000 01100101 01110010 01110011 01100101 01110110 01100101 01110010 01100101 00100000 01000011 01101111 01100100 01100101 00100000 01000011 01100001 01101101 01110000 00100001") 
# #should return "I love Persevere Code Camp!"