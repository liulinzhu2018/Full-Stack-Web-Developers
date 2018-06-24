import urllib

def read_text():
    quotes = open("C:\Python27\movie_quotes.txt")
    content = quotes.read()
    quotes.close()
    return content

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    print "output " +output
    connection.close()

    if "true"  in output:
        print "error, please check."
    else:
        print "ok"

content = read_text()
check_profanity(content)
