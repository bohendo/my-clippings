import sys
import getopt
import os


# works as a direct infile->outfile printer.
# need to add chapter information and sort the highlights by location...
# A lot of problems would be solved by adding some classes for chunks/books
# Create two modules:
# - one to read the infile into classes
# - one to print the classes to outfiles.
# Notes have locations that can be used to match them to their highlights
# I should record the start and end locations of each highlight so that
# ...I can more easily match any notes to them.

infile = 'My Clippings.txt'
return_pages = False
outfolder = "./outfolder/"


def main(argv):
    # default infile will be called My Clipping.txt based on kindle default
    global infile
    global return_pages

    # process command line arguments
    try:
        opts, args = getopt.getopt(argv, "i:p")
    except getopt.GetoptError:
        print "kipar -i <infile>"
        sys.exit()
    for opt, arg in opts:
        if opt == "-i":
            infile = arg
        if opt == "-p":
            return_pages = True

    # Initialize the output
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)

    # Initialize the input
    fin = open(infile, 'r')
    title = ""
    content = ""
    line = fin.readline()

    while (line != ""):
        # get rid of any blank/spacer lines before reading the title line
        while (line == "\n" or line == "==========\n"):
            line = fin.readline()

        # if we've got a new title, open a new file!
        if (title != getTitle(line)):
            print "new title!"
            title = getTitle(line)
            print title
            outfile = outfolder + title + ".txt"
            fout = open(outfile, 'a')

        # read the data line
        line = fin.readline()

        # What kind of content follows?
        notetype = getType(line)

        # If we're looking at a highlight, parse it
        if (notetype == "Highlight"):
            if (return_pages):
                location = str(getPage(line))
            else:
                location = str(getLocation(line))
            # read the blank like
            line = fin.readline()
            # read the rest of the chunk
            content = ""
            while (line != "==========\n"):
                content = content + line
                line = fin.readline()
            content = content.replace("\n", "")

        # If we're looking at a bookmark, say so and skip it for now
        if (notetype == "Bookmark"):
            print "Bookmark!"
            while (line != "==========\n"):
                line = fin.readline()

        # If we're looking at a note, say so and skip it for now
        if (notetype == "Note"):
            print "Note!"
            while (line != "==========\n"):
                line = fin.readline()

        if (return_pages):
            fout.write(" - \"" + content + "\" (page " + location + ")\n")
        else:
            fout.write(" - \"" + content + "\" (Location " + location + ")\n")

        line = fin.readline()

    # close files when we're done with them
    fin.close()
    fout.close()


# Input: a line (string) from kindle clippings describing the book title
# Output: A reformatted string describing the book title
# ie: given "xxxGetting Things Done: Productivity (Allen, David)"
#    return "Getting Things Done by David Allen"
# important things: need the location of "(", ")", ",", and ":"
def getTitle(strinput):
    # get rid of those first few weird characters
    for c in list(strinput):
        n = ord(c)
        if (n > 64 and n < 91 or n > 96 and n < 123):
            n = strinput.index(c)
            break
    # get the start of the subtitle, indicated by the first , or ;
    subtit_start = min(getFirstIndexOf(strinput, ":"),
                       getFirstIndexOf(strinput, ","))
    if subtit_start == getLastIndexOf(strinput, ","):
        subtit_start = None

    auth_start = getLastIndexOf(strinput, "(")

    if (getLastIndexOf(strinput, ";") is None):
        auth_end = getLastIndexOf(strinput, ")")
    else:
        auth_end = min(getLastIndexOf(strinput, ")"),
                       getLastIndexOf(strinput, ";"))

    if (auth_start is None or auth_end is None):
        print "Fatal error: wrong line passed to getTitle():"
        print strinput
        sys.exit()

    if (subtit_start is None):
        title = strinput[n:auth_start].strip()
    else:
        title = strinput[n:subtit_start].strip()

    auth = strinput[auth_start:auth_end]

    last_name_end = getFirstIndexOf(auth, ",")
    if (last_name_end is None):
        firstname = auth[1:]
        output = title + " by " + firstname
    else:
        firstname = auth[last_name_end+1:].strip()
        lastname = auth[1:last_name_end].strip()
        output = title + " by " + firstname + " " + lastname

    output = output.replace(" ", "_")
    output = "".join(ch for ch in output if ch.isalnum() or ch == "_")
    return output


def getFirstIndexOf(string, substring):
    if substring in string:
        return string.index(substring)
    else:
        # print substring + " not found in: " + string
        return None


def getLastIndexOf(string, substring):
    if substring in string:
        return string.rfind(substring)
    else:
        # print substring + " not found in: " + string
        return None


def getPage(strinput):
    try:
        a = strinput.index("page")
        b = strinput.index("|")
        return int(strinput[a+5:b])
    except:
        print "Fatal Error: wrong line passed to getPage():"
        print strinput
        sys.exit()


def getLocation(strinput):
    try:
        a = strinput.index("Location")
        b = strinput[1:].index("-")+1
        return int(strinput[a+9:b])
    except:
        print "Fatal Error: wrong line passed to getLocation():"
        print strinput
        sys.exit()


def getType(strinput):
    a = strinput[7:].index(" ")
    return strinput[7:a+7]

if __name__ == "__main__":
    main(sys.argv[1:])
