import array

ba = array.array('i', range(10**6))
bl = list(range(10**6))

import sys
print(100*sys.getsizeof(ba)/sys.getsizeof(bl))

