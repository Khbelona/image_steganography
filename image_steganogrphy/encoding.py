import stepic
from PIL import Image
from cryptography.fernet import Fernet

print("------------------------------")
key = Fernet.generate_key() #here we generate random key
print(f"Key for hidding data: {key}")

# Save the key to a file as encryption_key.txt
with open("encryption_key.txt", "wb") as key_file:
    key_file.write(key)

enc = Fernet(key)
text = input("Hidden data: ") # here we write our secret information
text_enc = enc.encrypt(text.encode())
file = input("photo: ") # here we type our photto(cover) path

img = Image.open(file)
img_stegano = stepic.encode(img, text_enc)  # here we hide our text in the image
img_stegano.save("stegano.png")  # we save the new image as stegano.png we created (extension = png)
output_image_path = "stegano.png"
img_stegano.save(output_image_path)
print("--------------------------------")
input("COMPLETE (PRESS enter -> exit)")

# here we open and show the output image
output_img = Image.open(output_image_path)
output_img.show()