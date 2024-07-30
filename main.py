#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(description='Takes data and shift as input')
parser.add_argument('data', metavar='data', type=str, help='Enter your data')
parser.add_argument('shift', metavar='shift', type=int, help='Enter the shift')
args = parser.parse_args()

data = args.data
shift = args.shift

# data = input("Enter the Data to encrypt: ")
# shift = int(input("Enter shift number (+ve or -ve): "))

if shift == 0:
    print("cipher_text: " + data)

# alpha = "abcdefghijklmnopqrstuvwxyz"

cipher_text = ""
for c in data:
    ascii = ord(c)
    # print(ascii)
    ascii = ascii + shift
    if 'a' <= c <= 'z':
        # our range is 97 to 122 inclusive
        if ascii > 122:
            ascii = 96 + (ascii-122)
        elif ascii < 97:
            ascii = (ascii-97) + 123
        # print(chr(ascii))
        cipher_text += chr(ascii)
    elif 'A' <= c <= 'Z':
        # our range is 65 to 90 inclusive
        if ascii > 90:
            ascii = 64 + (ascii-90)
        elif ascii < 65:
            ascii = (ascii-65) + 91
        # print(chr(ascii))
        cipher_text += chr(ascii)
    else:
        cipher_text += c


print("cipher_text after shift: " + cipher_text)

    
