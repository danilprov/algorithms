import time
import signal
from SingleArray import SingleArray
from VectorArray import VectorArray
from FactorArray import FactorArray
from MatrixArray import MatrixArray


class TimeoutException(Exception):  # Custom exception class
    pass


def timeout_handler(signum, frame):  # Custom signal handler
    raise TimeoutException


# Change the behavior of SIGALRM
signal.signal(signal.SIGALRM, timeout_handler)


def testPut(array, total):
    start_time = time.time() * 1000.
    for j in range(0, total):
        array.put(j)

    print(f'{array} + testPut: {total} - {round(time.time() * 1000. - start_time)}')


def testPutwithIndex(array, total, index=0):
    start_time = time.time() * 1000.
    for j in range(0, total):
        array.put(j, index)

    print(f'{array} + testPutwithIndex: {total} - {round(time.time() * 1000. - start_time)}')


def testRemove(array, total, index=0):
    start_time = time.time() * 1000.
    for j in range(0, total):
        array.remove(index)

    print(f'{array} + testRemove: {total} - {round(time.time() * 1000. - start_time)}')


single = SingleArray()
vector = VectorArray(1000)
factor = FactorArray()
matrix = MatrixArray()
TIMEOUTCAP = 60

for i in range(1, 6):
    for array in [single, vector, factor, matrix]:
        n = 10 ** i
        signal.alarm(TIMEOUTCAP)
        try:
            testPut(array, n)
        except TimeoutException:
            print(f'{array} + testPut: timed out after {TIMEOUTCAP} seconds')
        else:
            signal.alarm(0)
print('\n')

for i in range(1, 6):
    for array in [single, vector, factor]:
        n = 10 ** i
        signal.alarm(TIMEOUTCAP)
        try:
            testPutwithIndex(array, n)
        except TimeoutException:
            print(f'{array} + testPut: timed out after {TIMEOUTCAP} seconds')
        else:
            signal.alarm(0)
