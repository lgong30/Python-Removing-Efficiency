setup = """\
from test import remove_with_move, efficient_remove, remove
import numpy as np
n = 1000000
myList = range(n)
r = int(0.8*n)
removalIndices = sorted(np.loadtxt('perm.txt', dtype=int).tolist()[::r])
"""
setup2 = """\
from test import remove_with_move, efficient_remove, remove
import numpy as np
n = 1000000
myList = range(n)
r = int(0.8*n)
removalIndices = set(sorted(np.loadtxt('perm.txt', dtype=int).tolist()[::r]))
"""
setup3 = """\
from test import remove_with_move, efficient_remove, remove
import numpy as np
n = 1000000
myList = range(n)
r = int(0.8*n)
removalIndices = np.loadtxt('perm.txt', dtype=int).tolist()[::r]
"""
