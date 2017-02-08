setup = """\
from test import remove_with_move, efficient_remove, remove
n = 1000000
myList = range(n)
r = int(0.8*n)
removalIndices = range(r)
"""
setup2 = """\
from test import remove_with_move, efficient_remove, remove
n = 1000000
myList = range(n)
r = int(0.8*n)
removalIndices = set(range(r))
"""