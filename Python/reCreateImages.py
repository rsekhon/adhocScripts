#!/usr/bin/python3

import base64

targetDir = '/Users/rsekhon/Documents/Python/imagesDir/'

dataFile = 'fadRun.txt'

with open(dataFile, 'r') as dF:
    for line in dF:
       n,f,l,i = line.split('|')
      # print(i)
       outFileName = targetDir + str(n) + ".jpg"
       print(outFileName)
       base64_image_bytes = i.encode('utf-8')
       tF = open(outFileName, 'wb')
       tF.write(base64.decodebytes(base64_image_bytes))
       tF.close()
