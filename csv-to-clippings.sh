#!/bin/bash

# Transforms my-clippings.csv into My Clippings.txt

input="my-clippings.csv"
output="My Clippings.txt"

if [[ ! -f "$input" ]]; then
  echo "Nothing to coalesce"
  exit 1
fi
if [[ -f "$output" ]]; then
  echo "coalesce My\ Clippings.txt into my-clippings.txt first"
  exit 1
fi

dos2unix $input 2> /dev/null

title=`cat "$input" | sed '2q;d' | sed 's/^"//' | sed 's/",,,$//'`
author=`cat "$input" | sed '3q;d' | sed 's/^"//' | sed 's/",,,$//'`

tail -n +9 "$input" > "$input.clean"

while read line; do

  loc=`echo $line | awk -F "\",\"" '{print $2}' | tr -d '"'`
  hlt=`echo $line | awk -F "\",\"" '{print $4}' | tr -d '"'`

  echo "$title ($author)"
  echo "- Your Highlight on $loc | Added on Someday at Sometime PM"
  echo ""
  echo "$hlt"
  echo "=========="
  
done < "$input.clean" > "$output"

if [[ -f $output ]]; then
  rm "$input.clean" "$input"
fi

