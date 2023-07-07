import numpy as np
import control
import sys

def cnvStr(s):
    """Convert string to either int or float."""
    try:
        ret = int(s)
    except ValueError:
        #Try float.
        ret = float(s)
    return ret

num = np.array ([cnvStr(sys.argv[4]), cnvStr(sys.argv[3]), cnvStr(sys.argv[2]), cnvStr(sys.argv[1])])
den = np.array ([cnvStr(sys.argv[8]), cnvStr(sys.argv[7]), cnvStr(sys.argv[6]), cnvStr(sys.argv[5])])

W = control.tf(num, den)
#print(W)
ret = W.__call__(cnvStr(sys.argv[9]) * 1j) #argv[9] - msg from other node
print(ret)
                                                                                           
#What you print with the print() function will be sent back to JS like string

sys.stdout.flush()