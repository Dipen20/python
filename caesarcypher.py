print("Welcome to the caesar cipher")
#caesarcipher

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode'encryption and 'decode' for decryption\n")
text=input("Enter the text\n")
shift_number=int(input("Enter the shift_number\n"))

def encrypt(message,shift_amount):
        cipher_text=""
        for letter in message:
                position=alphabets.index(letter)
                new_postion=position+shift_amount
                cipher_text+=alphabets[new_postion]
               
        print(f"your encryptes message is{cipher_text}")

def decrypt(cipher_text,shift_amount):
        plain_text=" "
        for letter in cipher_text:
                position=alphabets.index(letter)
                new_position=position-shift_amount
                plain_text+=alphabets[new_position]
        print(f"your decrypted message is {plain_text}")
#encoding and deconding your password

if direction=="encode":
        encrypt(message=text,shift_amount=shift_number)
elif direction=="decode":
        decrypt(cipher_text=text,shift_amount=shift_number)
