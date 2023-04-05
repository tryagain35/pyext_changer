#!/usr/bin/env python

"""This simple script changes the extensions of the files in the folder where it's executed"""

__author__ = "tryagain_35"
__license__ = "Gnu GPL 3.0"
__version__ = "0.1"
__email__ = "tryagain_35@proton.me"

import os
import sys

def change_ext(old_ext, new_ext):
    for f in os.listdir():
        if os.path.splitext(f)[1] != ".py":
            if os.path.splitext(f)[1] == old_ext:
                os.rename(f, os.path.splitext(f)[0] + new_ext)

def main():
    if len(sys.argv) <= 2 or len(sys.argv) > 3:
        print("""Usage: extension_changer.py [.old_extension] [.new_extension] 
example: extension_changer.py .png .jpg""")
    else:
        change_ext(sys.argv[1], sys.argv[2])
        
if __name__ == '__main__':
    main()
