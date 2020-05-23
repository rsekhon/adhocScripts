#!/bin/bash

fTail='.jpg'
oDir='/Users/rsekhon/Documents/outImages/'

iF='outputFromFadRun.txt'

#			while IFS='\n' read list; do
cat $iF | 
while IFS='|' read n f l aD; do
    
    fN=$oDir$n$fTail
#	echo $fN
#	sleep 3
#	echo $aD
#	sleep 2
    echo $aD | base64 -d > $fN

done
