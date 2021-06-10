# This module is for parsing the command line arguments.

import argparse
import re
import os

def parseCmd():
    # Create the parser
    cmd_parser = argparse.ArgumentParser(prog='regexMathcer', description='Find matching lines in files or STDIN text using regex expression')

    # Add the supported arguments
    cmd_parser.add_argument('-r', '--regex', metavar='REGEXP', type=str, help='mandatory - the regular expression to search for.', required=True)
    cmd_parser.add_argument('-f', '--files', metavar='FILES', nargs='+', help='optional - a list of files to search in. If this parameter is omitted, the app expects text input from STDIN.')
    # mutually exclusive parameters
    exclusive = cmd_parser.add_mutually_exclusive_group()
    exclusive.add_argument('-c', '--color', action='store_const', const=1 ,help='optional - the matched text is highlighted in color [ANSI].')
    exclusive.add_argument('-u', '--underline', action='store_const', const=1, help='optional - "^" is printed underneath the matched text.')
    exclusive.add_argument('-m', '--machine', action='store_const', const=1, help='optional - print the output in the format: "file_name:line_number:start_position:matched_text".')

    args = cmd_parser.parse_args()
    pattern = args.regex
    files = args.files

    #check if regex is valid
    try:
        re.compile(pattern)
    except re.error:
        print('The regex expression is not valid, please use a valid pattern only !!!')
        exit()

    #check if existing files were given or STDIN text should be prompted
    if files is None:
        print()
        text = input("Please Enter text or Ctrl+c to quit:\n")
        if text == "":
            print("No text Found... quitting")
            exit()
        else:
            args.files = text
    else:
        for file in files:
            if not os.path.isfile(file):
                print(file,"does not exists or valid")
                exit()
    return args