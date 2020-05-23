#!/bin/bash

fTail='.jpg'
iDir='/Users/rsekhon/Documents/Images/'
uSr='root'
				#psWd=''
psWd='kj9MySqlRoot'
hoSt='localhost'
dB='fad'
firstLine=1

oF='outputFromFadRun.txt'

> $oF

/usr/local/mysql/bin/mysql -u"$uSr" -p"$psWd" -h"$hoSt" -D"$dB" -e'SELECT national_provider_id, first_name, last_name FROM doctor where has_profile_image = 1' 2>/dev/null |
 
# Read through the piped result until it's empty.
#			while IFS='\n' read list; do
while read n f l; do
    if [[ $firstLine -eq 1 ]]
    then
       firstLine=0
       continue
    fi
    fN=$iDir$n$fTail
    eS="$n|$f|$l|"

    if test ! -f $fN
    then
        echo "Image File for $n, $f, $l does not exist." >&2
	echo $eS >> $oF
	continue
    fi
	etext=`base64 $fN`
        echo $eS$etext >> $oF

done
