from numpy import True_
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
name = input('What is your name? >> ')

def greet(name):
    print(f'\n\nHello!! {name}. Welcome to \n\n{logo}')


def encode():
    e_msg = ""
    for i in msg:
        index = alphabet.index(i)
        e_index = index + shift
        e_letter = alphabet[e_index]
        e_msg += e_letter
    print(e_msg)


def decode():
    d_msg = ""
    for i in msg:
        index = alphabet.index(i)
        d_index = index - shift
        d_letter = alphabet[d_index]
        d_msg += d_letter
    print(d_msg)

greet(name)
end = False
while not end:
    todo = input("Enter 'encode' or 'decode' to encode or decode the message respectively >> ").lower()
    msg = input('Enter the message to Encode or Decode >> ').lower()
    shift = int(input("Enter the Shift Number >> "))
    if todo == "encode":
        encode()
    elif todo == "decode":
        decode()


    go_again = input("Enter 'yes' if you want to go again otherwise type 'no' to end >> ").lower()

    if go_again == "yes": continue
    elif go_again == "no":
        end = True