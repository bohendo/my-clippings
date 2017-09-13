# My Clippings

### `coalesce.sh`

This script will coalesce your "My Clippings.txt" files into one master file. While doing so, it removes any duplicate entries and sorts your highlights primarily by title and secondarily by the location/page.

The default output file is called my-clippings.txt but you can change the output variable to whatever you like.

`coalesce.sh` doesn't take any arguments but it expects to see a file called "My Clippings.txt" in the same folder.

After it's done, it will delete "My Clippings.txt" and leave you with an updated my-clippings file that contains all its highlights.

Usage looks like this:

```bash
$ ls
coalesce.sh  extract.pl  highlights  my-clippings.txt  My Clippings.txt  README.md

$ ./coalesce.sh 

$ ls
coalesce.sh  extract.pl  highlights  my-clippings.txt  README.md
```

### `extract.pl`

It separates the kindle-readable clippings monolith into a collection of files in the highlights directory which each contain all the highlights for one book in a much more human-readable format. This script does not take any arguments but it expects to see a file called "my-clippings.txt" in the same folder. 

Each book has a user-definable display name. When `extract.pl` encounters a book that's not in it's `highlights/.index.txt` file, it will prompt the user for a display title which will be used as the filename for that book's highlights. Empty display titles default to the book's full title but be careful, some of these are really long.

A display author is also asked for, this will be displayed at the top of this book's highlights file under the display title. This similarly uses the default value if none is provided.

Your choices are saved in `highlights/.index.txt` so you only need to provide this once once per book.

```bash
$ ./extract.pl my-clippings.txt 
New book: 'The Pragmatic Programmer: From Journeyman to Master' by 'Andrew Hunt;David Thomas'
Display title: Pragmatic Programmer
Display author: Andrew Hunt & David Thomas
```

Browse my highlights folder to see what the result looks like for yourself

