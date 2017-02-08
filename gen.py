import numpy as np

n = int(1e6)
r = int(0.8*n)


np.savetxt('perm.txt', np.random.permutation(n), fmt='%i')






