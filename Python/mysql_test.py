#!/usr/bin/python3

import base64
import pathlib
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="kj9MySqlRoot",
  database="fad"
)

# print(mydb)


mycursor = mydb.cursor()

mycursor.execute("SELECT first_name, last_name, national_provider_id FROM doctor WHERE has_profile_image = 1")

#mycursor.execute("SELECT first_name, last_name, national_provider_id FROM doctor")

myresult = mycursor.fetchall()

fS = '|'
imagesDir = '/Users/rsekhon/Documents/Images/'

outFile = 'fadRun.txt'

outfile = open(outFile, 'w') 

for f,l,n in myresult:
  fileName       = imagesDir + str(n) + ".jpg"
  path           = pathlib.Path(fileName)
  base64_message = ''
  if path.exists() and path.is_file():
#      print(fileName + " For " + f + " " + l + " Exists")


      with open(fileName, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')

      binary_file.close()
  else:
      print(fileName + " For " + f + " " + l + " Does Not Exist or is not a File")

  outstr = str(n) + fS + f + fS + l + fS + base64_message + '\n'
  outfile.write(outstr);

outfile.close()
mycursor.close()
