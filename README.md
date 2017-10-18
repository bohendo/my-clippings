# My Clippings

### `coalesce.sh`

This script will coalesce your `My Clippings.txt` files into one master file. While doing so, it removes any duplicate entries and sorts your highlights primarily by title and secondarily by the location/page. Note: sorting is handled by `supersort.py`.

The default output file is called my-clippings.txt but you can change the output variable to whatever you like.

`coalesce.sh` doesn't take any arguments but it will look in two places for a file called `My Clippings.txt`: the current directory and a directory called `/media/username/Kindle/documents` where username is the name of the user who runs this script (determined automatically). If no clippings files are found in either location, `coalesce.sh` proceeds to re-sort & re-clean `my-clippings.txt`

Usage looks like this:

```bash
$ ./coalesce.sh 
```

### `csv-to-clippings.sh`

If you have a kindle, you can open a book, tap `GO TO`, go to the `Notes` tab, and there is an `Export Notes` button at the bottom. If you export your notes, you'll get a csv file containing all your highlights for some book.

If you copy this csv to the my-clippings folder and rename it to 'my-clippings.csv' then this script will convert your clippings from csv format to the traditional format for `My Clippings.txt`. Then, you can `coalesce.sh` and `prettify.pl` it just like normal clippings.

Very useful if you go over your clipping limit for some book. You can delete clippings from earlier in the book and then export to regain access to clippings later in the book. Unfortunately, it's still a somewhat tedious & manual process that isn't easily scripted.

### `prettify.pl`

It separates the kindle-readable clippings monolith into a collection of files in the highlights directory which each contain all the highlights for one book in a much more human-readable format. This script does not take any arguments but it expects to see a file called "my-clippings.txt" in the same folder. 

Each book has a user-definable display name. When `prettify.pl` encounters a book that's not in it's `highlights/.index.txt` file, it will prompt the user for a display title which will be used as the filename for that book's highlights. Empty display titles default to the book's full title but be careful, some of these are really long.

A display author is also asked for, this will be displayed at the top of this book's highlights file under the display title. This similarly uses the default value if none is provided.

Your choices are saved in `highlights/.index.txt` so you only need to provide this once once per book.

```bash
$ ./prettify.pl my-clippings.txt 
New book: 'The Pragmatic Programmer: From Journeyman to Master' by 'Andrew Hunt;David Thomas'
Display title: Pragmatic Programmer
Display author: Andrew Hunt & David Thomas
```

Browse my highlights folder to see what the result looks like for yourself!

