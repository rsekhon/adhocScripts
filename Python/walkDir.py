import os
import sys
rootdir = sys.argv[1]

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print(os.path.join(subdir, file))
        # print("File is " + subdir + ' ' + file)
