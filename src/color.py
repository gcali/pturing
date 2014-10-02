#!/usr/bin/env python3

class Color:
    BOLD = '\033[1m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'

if __name__ == '__main__':
    print("I'm",Color.BOLD + "bold" + Color.END, "and",
          Color.UNDERLINE + "underlined" + Color.END)

