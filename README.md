# Automatic Password Generator

## Project Description
The **Automatic Password Generator** is a Python script that generates secure, random passwords based on user preferences. Users can customize the password length and choose whether to include numbers and special characters, making it suitable for various security requirements.

## Features
- Customizable password length.
- Option to include numbers in the password.
- Option to include special characters in the password.
- Generates strong, random passwords.
- Simple command-line interface.

## Requirements
- Python 3.x
- `pyperclip` library (optional, if clipboard functionality is needed)

You can install `pyperclip` using pip:
```bash
pip install pyperclip
```
## How to Use
1. Clone this respositary to your local machine:
```bash
  git clone https://github.com/GowthamBads/Automatic-Password-Generator.git
```
2. Navigate to the project directory:
```bash
 cd password-generator
```
3. Run the Python script:
```bash
 python password_generator.py
```
4. Follow the prompts to generate a password:
- Enter the minimum password length.
- Choose whether to include numbers (y/n).
- Choose whether to include special characters (y/n).
5. The generated password will be displayed on the screen and copied to your clipboard (if pyperclip is installed).
## Example Usage
 Enter password length: 12
 
 Include numbers? (y/n): y
 
 Include special characters? (y/n): y
 
 The Generated password is: 4a$z8c%t2n@v
