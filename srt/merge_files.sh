#!/bin/bash

RAW="merged"
NOTS="ds-nots"
DS="../ds.srt"

rm $RAW

for file in ./*.srt
do
   echo "Merging.... $file"
   more "$file" >> $RAW
   
done

grep -v ^[[:digit:]] $RAW > $NOTS
grep -v www $NOTS > $DS
