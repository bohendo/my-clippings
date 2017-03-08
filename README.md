# kipar - the **ki**ndle clippings **par**ser

Kindle highlights and notes are stored in a "My Clippings".txt file in an ugly format. This script copies your kindle notes to a format that's much easier to read. A kipar folder is created and filled with 1 file for each book you have highlights or notes for. Each file displays the title and author followed by a list of all of your notes/highlights sorted chronologically and labeled with the page or location it starts on.

Download `kipar.pl` and then run it like this.

```bash
perl /path/to/kipar.pl /path/to/My\ Clippings.txt
```

You can run it over and over on the same `My Clippings.txt` and your kipar library will not be filled with duplicate entries. That means you can throw all of your clippings into one archive folder, maybe update filenames with the date you added them. Then if you ever need to completely reset your kipar library you can run the following.

```bash
rm -rf /path/to/kipar/* && cat /path/to/clipping-archive/*.txt | /path/to/kipar.pl
```
