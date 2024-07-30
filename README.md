# Caesar-Cipher

A simple Python script to generate cipher text using a Caesar cipher method. This script can encrypt and decrypt text, and can handle both direct text input and file input.

## Features

- Can Encrypts and decrypts text using a Caesar cipher
- Handles both uppercase and lowercase letters
- Can take input directly or from a file
- Option to save the output to a file

## Installation

1. Ensure you have Python installed.
2. Clone the repository or download the script file.

```bash
git clone https://github.com/raghav2130/Caesar-Cipher.git
cd Caesar-Cipher
```
## Usage

The script can be used directly from the command line. Below are the options and arguments you can use:
Arguments

    data: The text to be encrypted or decrypted, or the path to the input file if --file is specified.
    shift: The number of positions to shift the characters.

## Options

    --file: Indicates that the data argument is a file path.
    --decrypt: Decrypts the input text.
    --output <output>: Specifies the output file path to save the result.

## Examples
### Encrypting Text

Encrypting the text "hello" with a shift of 3:

```bash
python caesar.py "hello" 3
```
Output:
```
Cipher text after shift: khoor
```


### Decrypting Text

Decrypting the text "khoor" with a shift of 3:
```bash
python caesar.py "khoor" 3 --decrypt
```
Output:
```bash
Cipher text after shift: hello
```

### Using a File for Input

Encrypting text from a file input.txt with a shift of 5:
```bash
python caesar.py input.txt 5 --file
```

Output:
```bash
Cipher text after shift: <encrypted content from input.txt>
```

### Saving Output to a File

Encrypting text "hello" with a shift of 3 and saving to output.txt:
```bash
python caesar.py "hello" 3 --output output.txt
```


Check the content of output.txt for the result.
