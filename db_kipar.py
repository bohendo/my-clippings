import sys
import getopt
import MySQLdb
import helper

# Need to add chapter information and sort the highlights by location...
# A lot of problems would be solved by adding some classes for chunks/books
# Create two modules:
# - one to read the infile into classes (and store in a database?)
# - one to print the classes to outfiles.
# Notes have locations that can be used to match them to their highlights
# I should record the start and end locations of each highlight so that
# ...I can more easily match any notes to them.
# install and get familiar with calibre to potentially get chapter info
# I need to get a better understanding of regular expressions
# I would like to access my MySQL database and store all my highlights in it


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

    fin = open(infile, 'r')
    line = fin.readline()
    print helper.getTitle(line)


if __name__ == "__main__":
    main(sys.argv[1:])
