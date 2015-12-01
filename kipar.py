import re
import codecs
import sys
import getopt
import MySQLdb



class Book:
    def __init__(self, title_tuple):
        # title_tuple = (title, lastname, firstname, addlastname, addfirstname)
        self.title = title_tuple[0].strip()
        # the author might night have a first name
        if title_tuple[2] is None:
            self.author = title_tuple[1]
        else:
            self.author = title_tuple[2] + " " + title_tuple[1]
        # add the additional author if available
        if title_tuple[3] is not None:
            self.addAuthor = title_tuple[3]
        elif title_tuple[3] is not None and title_tuple[4] is not None:
            self.addAuthor = title_tuple[4] + " " + title_tuple[3]
        # we'll add to these empty lists later
        self.highlights = []
        self.notes = []

    def addLength(self, pages, locations):
        self.pages = pages
        self.locations = locations

    def addHighlight(self, highlight):
        self.highlights.append(highlight)

    def addNote(self, note):
        self.notes.append(note)

    def toString(self):
        return self.title + " by " + self.author

    def getHighlights(self):
        output = ""
        for h in self.highlights:
            output = output + h.getContent() + h.getLocation() + "\n\n"
        return output


class Highlight:
    def __init__(self, loc_tuple, content):
        if loc_tuple[1] == "Location":
            self.page = None
            self.locStart = int(loc_tuple[2])
            self.locEnd = int(loc_tuple[3])
        elif loc_tuple[1] == "page":
            self.page = int(loc_tuple[2])
            self.locStart = int(loc_tuple[5])
            self.locEnd = int(loc_tuple[6])
        self.content = content

    def getContent(self):
        return self.content

    def getLocation(self):
        return "(Location " + str(self.locStart) + "-" + str(self.locStart) + ")"


class Note:
    def __init__(self, loc_tuple, content):
        if loc_tuple[1] == "Location":
            self.page = None
            self.locStart = int(loc_tuple[2])
        elif loc_tuple[1] == "page":
            self.page = int(loc_tuple[2])
            self.locStart = int(loc_tuple[5])
        self.content = content

    def getContent(self):
        return self.content


def main(argv):
    infile = "My Clippings.txt"
    # process command line arguments
    try:
        opts, args = getopt.getopt(argv, "i:")
    except getopt.GetoptError:
        print "kipar -i <infile>"
        sys.exit()
    for opt, arg in opts:
        if opt == "-i":
            infile = arg
    library = []
    with codecs.open(infile, mode='r', encoding="UTF-8") as fin:
        while True:
            currBook = Book(parseTitle(fin.readline()))
            # if parseTitle returned "fatal error", we're done
            if currBook.toString() == "F by t a":
                break
            # if this book isn't in our library yet, add it
            if currBook.toString() not in map(Book.toString, library):
                library.append(currBook)
            # if it is, get the item from library with the same index as
            # currBook.toString() has in the library of strings
            else:
                currBook = library[
                    map(Book.toString, library).index(currBook.toString())
                ]
            loc = parseLocation(fin.readline())
            content = ""
            while True:
                temp = parseContent(fin.readline())
                if temp is True:
                    break
                if temp is False:
                    return "error, unexpected break"
                else:
                    content = content + temp
            if loc[0] == "Highlight":
                currBook.addHighlight(Highlight(loc, content))
            elif loc[0] == "Note":
                currBook.addNote(Note(loc, content))

    print
    for b in library:
        print "=============================="
        print b.toString()
        print "=============================="
        print str(b.getHighlights())

# `index` table in library database
# +----+---------------------+-------------+-------+-----------+------------+
# | ID | Title               | Author      | Pages | Locations | AddAuthors |
# +----+---------------------+-------------+-------+-----------+------------+
# |  1 | The 4-Hour Workweek | Tim Ferriss |  NULL |      6768 | NULL       |
# |  2 | Getting Things Done | David Allen |  NULL |      5847 | NULL       |
# +----+---------------------+-------------+-------+-----------+------------+

    # connect to mysql
    mysqldb = MySQLdb.connect(host="localhost",
                              user="rojahend",
                              passwd="password",
                              db="library")
    cursor = mysqldb.cursor()
    # get the current list of books in the library
    try:
        cursor.execute("SELECT title FROM `index`;")
        index = []
        for t in cursor.fetchall():
            index.append(t[0])
    except:
        print "error getting library data"
        sys.exit()
    print


def parseContent(strinput):
    if strinput == '==========\r\n':
        return True
    if strinput == "\r\n":
        return ""
    # this catches the end of the file
    if strinput == "":
        return False
    else:
        return cleanup(strinput)


def parseTitle(strinput):
    strinput = cleanup(strinput)
    # sample strinput:
    # ???Smarts: The Art (Science?) of Work (Allen, David; Gates, Bill)
    output = []
    div = strinput.rfind('(')
    title = strinput[:div]
    author = strinput[div:]
    # sample title: """???Smarts: The Art (Science?) of Work """
    pattern = """
    ([\w '-]+)  # matches the title
    ,?          # there might be a subtitle separated by a comma
    :?          # or the subtitle might be separated by a colon
    [\w -]*     # subtitle
    """
    match = re.compile(pattern, re.VERBOSE).search(title)
    if match:
        output.extend(match.groups())
    else:
        return "Fatal error: couldn't parse Title..."
    # sample author: "(Allen, David; Gates, Bill)\n"
    # sample author: "(Unknown)\n"
    pattern = """
    \(          # start of the author chunk
    ([\w. ]+)   # author last name (or only name?)
    ,?\s?       # author separator
    ([\w. ]+)?  # author first name
    ;?          # coauthor separator
    ([\w. ]+)?  # coauthor last name
    ,?\s?       # coauthor separator
    ([\w. ]+)?  # coauthor first name
    \)          # end of the author chunk
    """
    match = re.compile(pattern, re.VERBOSE).search(author)
    if match:
        output.extend(match.groups())
    else:
        return "Fatal error: couldn't parse Author..."
    return output


def parseLocation(strinput):
    strinput = cleanup(strinput)
    # sample strinputs:
    # - Your Highlight on page 12 | Location 550-551 | Added whenever...
    # - Your Highlight on Location 550-551 | Added whenever...
    # - Your Note on Location 1043 | Added whenever
    # - Your Note on page 139 | Location 1517 | Added
    pattern = """
    ^-\sYour\s       # matches the beginning of location lines
    (\w+?)           # content type (ie Highlight, Bookmark, Note)
    \son\s           # filler, always matches " on "
    (page|Location)  # does this line contain a page number?
    \s(\d+)-?        # page number OR location number
    (\d*)            # second location number if it exists
    \s\|\s           # filler, always matches " | "
    (Location|Added) # If there's still data here, it'll be Location data
    \s(\d*)-?        # first location number if it exists
    (\d*)            # second location number if it exists
    """
    match = re.compile(pattern, re.VERBOSE).match(strinput)
    if match:
        return match.groups()
    else:
        return "Fatal error: couldn't parse Location..."


# let's dumb down kindle's fancy characters
def cleanup(strinput):
    strinput = strinput.replace(u'\u2014', '-')
    strinput = strinput.replace(u'\u2013', '-')
    strinput = strinput.replace(u'\u2018', "'")
    strinput = strinput.replace(u'\u2019', "'")
    strinput = strinput.replace(u'\u201c', '"')
    strinput = strinput.replace(u'\u201d', '"')
    strinput = strinput.replace(u'\ufeff', '')
    # anything not caught above can just be removed
    return re.sub('[^\n\r -~]', '', strinput)


if __name__ == "__main__":
    main(sys.argv[1:])
