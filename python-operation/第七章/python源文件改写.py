import keyword
stopwords = '\t\n\r: ()'
functionwords = '.('
word = []
output = ''
lastAvailable = ['from', 'import']
last = False
def readFile(path):
    file = open(path,'r',encoding = 'utf-8')
    string = file.read()
    return string[1:]
def parse(string):
    global word
    global output
    for i in string:
        if i in stopwords:
            wd = ''.join(word)
            res = isKeyWord(wd)
            if res == False:
                if i not in functionwords and last == False:
                    wd = wd.upper()
            if wd in lastAvailable:
              last = True
            else:
                last = False
            output += wd
            output += i
            word = []
        else:
            word.append(i)
def isKeyWord(string):
    if string in keyword.kwlist:
        return True
    return False
def outPutFile():
    file = open('flie路径','w',encoding = 'utf-8')
    file.write(output)

string = readFile('flie路径')
parse(string)
outPutFile()