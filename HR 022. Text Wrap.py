# Text Wrap

import textwrap
def wrap(string, max_width):
    a =  textwrap.fill(string, max_width)
    return a      

wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4)

'''
Expected output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
