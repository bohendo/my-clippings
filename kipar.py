import codecs
import sys
import getopt
# import MySQLdb
import kipar_helper

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
    # with open(infile, mode='r') as fin:
    with codecs.open(infile, mode='r', encoding="UTF-8") as fin:
        while True:
            title = kipar_helper.parseTitle(fin.readline())
            loc = kipar_helper.parseLocation(fin.readline())
            content = ""
            while True:
                temp = kipar_helper.parseContent(fin.readline())
                # print repr(temp)
                if temp is True:
                    break
                if temp is False:
                    return
                else:
                    content = content + temp
            # instead of printing, I would like save this info in objects.
            # also, I would like this to print double quotes instead of
            # ...weird nonstandard characters. goddamn it kindle.
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


if __name__ == "__main__":
    main(sys.argv[1:])
