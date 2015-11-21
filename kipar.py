import re
import codecs
import sys
import getopt
# import MySQLdb
# import kipar_helper

# read this if you want: https://docs.python.org/2/howto/unicode.html


def main(argv):
    print
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
    finLooper(infile)


def finLooper(infile):
    with codecs.open(infile, mode='r', encoding="UTF-8") as fin:
        while True:
            title = parseTitle(fin.readline())
            loc = parseLocation(fin.readline())
            content = ""
            while True:
                temp = parseContent(fin.readline())
                if temp is True:
                    break
                if temp is False:
                    return
                else:
                    content = content + temp
            # instead of printing, I would like save this info in objects.
            print title[0], "by", title[2], title[1]
            print loc[0], "on page", loc[1], "locations:", loc[2], "-", loc[3]
            print content
            print
    # connect to mysql
    # mysqldb = MySQLdb.connect(host="localhost",
    #                           user="rojahend",
    #                           passwd="password",
    #                           db="library")
    # cursor = mysqldb.cursor()
    # get the current list of books in the library
    # try:
    #     cursor.execute("SELECT title FROM `index`;")
    #     index = []
    #     for t in cursor.fetchall():
    #         index.append(t[0])
    # except:
    #     print "error getting library data"
    #     sys.exit()
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
        if re.sub('[\n\r -~]', '', strinput) == '':
            return strinput
        else:
            # let's dumb down kindle's fancy characters
            strinput = strinput.replace(u'\u2014', '-')
            strinput = strinput.replace(u'\u2013', '-')
            strinput = strinput.replace(u'\u2018', "'")
            strinput = strinput.replace(u'\u2019', "'")
            strinput = strinput.replace(u'\u201c', '"')
            strinput = strinput.replace(u'\u201d', '"')
            return strinput


def parseTitle(strinput):
    # sample strinput:
    # ???Smarts: The Art (Science?) of Work (Allen, David; Gates, Bill)
    output = []
    div = strinput.rfind('(')
    title = strinput[:div]
    author = strinput[div:]
    # sample title: """???Smarts: The Art (Science?) of Work """
    pattern = """
    ([\w -]+)   # matches the title
    ,?          # there might be a subtitle separated by a comma
    :?          # or the subtitle might be separated by a colon
    [\w -]+     # subtitle
    """
    match = re.compile(pattern, re.VERBOSE).search(title)
    if match:
        output.extend(match.groups())
    else:
        return "Fatal error: couldn't parse Title..."
    # sample author: """(Allen, David; Gates, Bill)\n"""
    pattern = """
    \(          # start of the author chunk
    (\w+)       # author last name
    ,[ ]        # author separator
    ([\w. ]+)   # author first name
    ;?          # coauthor separator
    (\w+)?      # author last name
    ,?[ ]?      # author separator
    (\w+)?      # author first name
    \)          # end of the author chunk
    """
    match = re.compile(pattern, re.VERBOSE).search(author)
    if match:
        output.extend(match.groups())
    else:
        return "Fatal error: couldn't parse Author..."
    return output


def parseLocation(strinput):
    # sample strinput:
    # - Your Highlight on page 12 | Location 550-551 | Added whenever...
    pattern = """
    ^-\ Your # matches the beginning of location lines
    \ (\w+)  # content type (ie Highlight, Bookmark, Note)
    .*?      # will usually match: " on page "
    (\d+)    # page number
    \W+\w+   # will usually match: " | Location"
    \ (\d+)  # location start
    -?       # location separator
    (\d+)?   # location end
    """
    match = re.compile(pattern, re.VERBOSE).match(strinput)
    if match:
        return match.groups()
    else:
        return "Fatal error: couldn't parse Author..."


if __name__ == "__main__":
    main(sys.argv[1:])
