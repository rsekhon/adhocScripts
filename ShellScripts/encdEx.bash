#!/bin/bash
echo "Enter Some text to encode"
	read text
etext=`echo -n $text | base64`
	echo "Encoded text is : $etext"

dtext=`echo -n $etext | base64 -d`
	echo "Re Decoded text is : $dtext"
