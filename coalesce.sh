#!/bin/bash

# If our kindle is plugged in, let's grap clippings from it
if [[ -f "/media/`whoami`/Kindle/documents/My Clippings.txt" ]]
then
  input="/media/`whoami`/Kindle/documents/My Clippings.txt"

# Otherwise look for clippings in the current dir
elif [[ -f "/Volumes/Kindle/documents/My Clippings.txt" ]]
then
  input="/Volumes/Kindle/documents/My Clippings.txt"

else
  input="My Clippings.txt"
fi

echo "Preparing to parse input: $input"
sleep 2

# Move $output to a temporary read location so we can 
#   write to this filename at the other end of our pipe
output="my-clippings.txt"
if [[ -f "$output" ]]; then mv "$output" ".$output.backup"
fi

# Send our input and old output into the pipe
cat "$input" ".$output.backup" |\

# Remove byte order markers
sed 's/^\xef\xbb\xbf//' |\

# Transform everything into one giant line
tr -d '\n\r' |\

# Split every highlight/bookmark/note onto it's own line
# anchor to end of delimiter in case highlight ends with =
sed 's/==========\([^=]\)/==========\n\1/g' |\

# Super sort will sort these lines
#   primarily by title to group books together
#   secondarily by page/location to put each book in order
python3 supersort.py |\

# Remove any duplicate lines (we're idempotent!)
uniq |\

# Remove any lines that have been throttled by DRM
sed '/<You have reached the clipping limit for this item>/d' |\

# Put the newlines back where they were originally and we're done
sed 's/==========$/\n==========/g' |\
sed 's/ \([AP]M\)/ \1\n\n/'        |\
sed 's/- Your/\n- Your/'           \
> "$output"
# change above to a temp file to debug

# Remove our old output if everything went well
if [[ -f "$output" ]]; then
  rm ".$output.backup"

# Reverting changes makes debugging cleaner
else
  echo "Expected output not generated, reverting changes.."
  mv ".$output.backup" "$output"
fi

