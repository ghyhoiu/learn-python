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
print("hello world")