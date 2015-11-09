
class Highlight:
    """Stores text and identifying info from one highligted region"""

    def __init__(self, startLoc, endLoc, page, content):
        self.startLoc = startLoc
        self.endLoc = endLoc
        self.page = page

    def addContent(self, content):
        self.content = content

    def addNote(self, note):
        self.note = note

    def containsLoc(self, location):
        if location > self.startLoc and location < self.endLoc:
            return True
        else:
            return False


class Book:
    """Stores a list of highlights associated with the given book"""

    def __init__(self, title):
        self.title = title
        self.loh = []
        self.lon = []
        self.firstName = ""
        self.lastName = ""

    def setAuthor(self, first, last):
        self.firstName = firstName
        self.lastName = lastName

    def hasAuthor():
        if (firstName == "" and lastName == ""):
            return false
        else:
            return true

    # I want to insert-sort the highlights as I recieve them.
    def addHighlight(self, highlight):
        self.loh.append(highlight)

    def addNote(self, content, location):
        # search loh for a highlight that
        for h in self.loh:
            if h.containsLoc(location):
                h.addNote(content)
            else:
                self.lon.append(content)

    def getTitle():
        return self.title
