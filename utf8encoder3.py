#!/usr/bin/python3
import sys
import os

def main():
    byteBuffer = 2
    path = os.path.expanduser(sys.argv[1])
    fin = open(path,"rb")
    fout = open("utf8encoder_out.txt",'w+b')
    Buffer = fin.read(byteBuffer) 
    
    while len(Buffer):
        charRange = int.from_bytes(Buffer, byteorder='big')
        data = encodeChar(charRange)
        fout.write(data)
        Buffer = fin.read(byteBuffer)
    
#     print('Done!')
    
def encodeChar(charRange):
    bytesOfChar_8 = 0
    
    if(charRange <= 127):
#         print('One Byte')
        inputBinChar = bin(charRange)
        inputLength = len(inputBinChar)
        
        byteOne = "0" + (inputBinChar[-(inputLength-2):])
        
        charBytes = int(byteOne,2)
        bytesOfChar_8 = bytesOfChar_8 | charBytes
#         print('UTF-8 byte ::', bin(bytesOfChar_8))
        return bytesOfChar_8.to_bytes(1, 'big')
         
    elif(charRange > 127 and charRange <= 2047):
#         print('Two Bytes')
        
        setBits = int('1100000010000000',2)
        bytesOfChar_8 = bytesOfChar_8 | setBits
        inputBinChar = bin(charRange)
        inputLength = len(inputBinChar)
        
        byteOne = "000" + (inputBinChar[-(inputLength-2):-6]) 
        byteTwo = "00" + (inputBinChar[-6:])
        
        charBytes = int(byteOne + byteTwo,2)
        bytesOfChar_8 = bytesOfChar_8 | charBytes
#         print('UTF-8 byte ::', bin(bytesOfChar_8))
        return bytesOfChar_8.to_bytes(2, 'big')
    
    elif(charRange > 2047 and charRange <= 65535):
#         print('Three Bytes')
        
        setBits = int('111000001000000010000000',2)
        bytesOfChar_8 = bytesOfChar_8 | setBits
        inputBinChar = bin(charRange)
        inputLength = len(inputBinChar)
        
        byteOne = "0000" + (inputBinChar[-(inputLength-2):-12]) 
        byteTwo = "00" + (inputBinChar[-12:-6])
        byteThree = "00" + (inputBinChar[-6:])
        
        charBytes = int(byteOne + byteTwo + byteThree, 2)
        bytesOfChar_8 = bytesOfChar_8 | charBytes
#         print('UTF-8 byte ::', bin(bytesOfChar_8))
        return bytesOfChar_8.to_bytes(3, 'big')
        
    else:
        print('Sorry, This application supports encoding to maximum 3 Bytes Only.')
    

if __name__ == "__main__":main()
