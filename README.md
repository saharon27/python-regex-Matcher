# python-regex-Matcher

Simple Python3 script that allow to search regex expression in files or text.

## Usage

This app can be run out-of-the-box by running:
```
python src/main.py <parameters>
```

or by building the pacakge:
```
python setup.py install
```
this will allow to use the script as console script
```
regmatcher <parameters>
```


## How to use the script
running the script with -h flag will show the following help screen:

```
Find matching lines in files or STDIN text using regex expression

optional arguments:
  -h, --help            show this help message and exit
  -f FILES [FILES ...], --files FILES [FILES ...]
                        optional - a list of files to search in. If this parameter is omitted, the app expects text input
                        from STDIN.
  -c, --color           optional - the matched text is highlighted in color [ANSI].
  -u, --underline       optional - "^" is printed underneath the matched text.
  -m, --machine         optional - print the output in the format: "file_name:line_number:start_position:matched_text".

required arguments:
  -r REGEXP, --regex REGEXP
                        mandatory - the regular expression to search for.
```

## Windows support

This script can be used cross-platform. but in windows if you wish to color the matching string you will need to use colorama module.
Just un-comment the following lines in src/regex_search.py
```
#from colorama import init, Fore, Style
#init()
```
after that please install the module:
```
pip install colorama
```

and you are all set.
