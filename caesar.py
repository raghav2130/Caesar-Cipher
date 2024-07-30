#!/usr/bin/python
import argparse

def cipher_generator(data, shift):
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
    return cipher_text

parser = argparse.ArgumentParser(description='Takes data and shift as input')
parser.add_argument('--file', action='store_true', help='Indicate if the data argument is a file path')
parser.add_argument('--decrypt', action='store_true', help='Decrypt the data')
parser.add_argument('--output', metavar='output', type=str, help='Output file path to save the result')
parser.add_argument('data', metavar='data', type=str, help='Enter your data')
parser.add_argument('shift', metavar='shift', type=int, help='Enter the shift')
args = parser.parse_args()

if args.file:
    with open(args.data, 'r') as file:
        data = file.read().strip()
else:
    data = args.data

shift = args.shift

if args.decrypt:
    shift = -shift


# alpha = "abcdefghijklmnopqrstuvwxyz"

if shift == 0:
    result = data
else:
    result = cipher_generator(data, shift)

if args.output:
    with open(args.output, 'w') as file:
        file.write(result)
else:
    print("Cipher text after shift: " + result)

    
