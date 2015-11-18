import re
# import sys


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
            strinput = strinput.replace(u'\u201c', '"')
            strinput = strinput.replace(u'\u201d', '"')
            strinput = strinput.replace(u'\u2019', "'")
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
