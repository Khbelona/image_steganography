import stepic
from PIL import Image
from cryptography.fernet import Fernet

print("-------------------------------------")
key = input("Enter the decryption key: ")  # enter the decryption key that encryption_key.txt

# heree we read the encryption key from the file(encryption_key.txt)
with open("encryption_key.txt", "r") as key_file:
    expected_key = key_file.read().strip()

# here we check if the entered key does not match the expected key
if key != expected_key:
    print("ERROR: Decryption key does not match the expected key.")
else:
    dec = Fernet(key)
    file = input("Enter the path of the photo: ")#here we type our stegano image path
    img = Image.open(file)#here we open our stegano image path(stegano.png)
    decode = stepic.decode(img)  # Here we take the text out of hiding
    text_dec = dec.decrypt(decode.encode())  # Here we decrypt the text
    print("Decrypted message is: " + text_dec.decode()) # here we get our secret information
    
print("-----------------------------------")
