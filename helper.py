import re


def getTitle(strinput):
    print "strinput = " + strinput
    pattern = re.compile('\(?\w+:?,?\)?')
    match = pattern.findall(strinput)
    # match = pattern.search(strinput)
    if match:
        return match
    else:
        return "no match"
