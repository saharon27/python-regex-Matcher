import cmdParse
import regex_search


def main():
    args = cmdParse.parseCmd()
    regex_search.startSearching(args)


if __name__ == '__main__':
    main()      
    