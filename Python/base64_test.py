#!/usr/bin/python3

import base64

# Ascii to base64

message = "Here we have to read in the file or something"
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

# print(base64_message)

# base64 to Ascii

backtobytes = base64_message.encode('ascii')
eightbits = base64.b64decode(backtobytes)
readableMsg = message_bytes.decode('ascii')

# print(readableMsg)

# Binary File to Base64

with open('/Volumes/BLUE16/melinda/Images/iMages/1316904725.jpg', 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')

    print(base64_message)

binary_file.close()

# Base64 to File

base64_img = ''

with open('imageFile.txt', 'r') as imgTxt:
    base64_img = imgTxt.read()

imgTxt.close()

base64_img_bytes = base64_img.encode('utf-8')

with open('decoded_image.jpg', 'wb') as file_to_save:
    decoded_image_data = base64.decodebytes(base64_img_bytes)
    file_to_save.write(decoded_image_data)

file_to_save.close()
