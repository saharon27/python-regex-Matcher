import re
#To add support for windows coloring un-comment those lines
#from colorama import init, Fore, Style
#init()

def startSearching(arguments):
    # Compiling the pattern object and reuse the compiled object over and over in the loop
    pattern = re.compile(arguments.regex)
    #Checking for special style flags
    deco=""
    if arguments.color is not None:
        deco = "color"
    if arguments.underline is not None:
        deco = "underline"
    if arguments.machine is not None:
        deco = "machine"
    #checking for files or text input and running the search
    if type(arguments.files) == str:
        txt = arguments.files
        searchForMatch("STDIN", pattern, txt, deco)
    if type(arguments.files) == list:
        for file in arguments.files:
            f = open(file, 'r')
            txt = f.read()
            searchForMatch(file ,pattern, txt, deco) 
    

def searchForMatch(nameOfFile, pattern, fullText, style):
    index=0
    resetColor = '\033[0m' #RESET COLOR
    forecolor = '\033[96m' #CYAN
    for line in fullText.splitlines():
        result = re.search(pattern, line)
        if result is not None:
            if style == "color":
                splittedResult = line.split(result.group())
                prefixForfullPrint = "{} Line: {} - Line is: ".format(nameOfFile,index)
                print(prefixForfullPrint, splittedResult[0], forecolor + result.group() + resetColor, splittedResult[1])
            if style == "underline":
                splittedResult = line.split(result.group())
                prefixForfullPrint = "{} Line: {} - Line is: ".format(nameOfFile,index)
                print(prefixForfullPrint, splittedResult[0], result.group(), splittedResult[1])
                underlinePrint(prefixForfullPrint, splittedResult,result.group())
            if style == "machine":
                prefixForfullPrint = "{}:{}:".format(nameOfFile,index)
                print(prefixForfullPrint + result.group())
            if style == "":
                prefixForfullPrint = "{} Line: {} - Line is: ".format(nameOfFile,index)
                print(prefixForfullPrint + result.string)
        index+=1

def underlinePrint(fullPrefix, text,match):
    underlineChar = '^'
    fullPrefixlen = len(fullPrefix)
    prefixlen = len(text[0])
    matchlen = len(match)
    suffixlen = len(text[1])
    print(' ' * fullPrefixlen, ' ' * prefixlen,underlineChar * matchlen,' ' * suffixlen)
