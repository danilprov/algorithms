import os
import glob
import time
import signal


class TimeoutException(Exception):  # Custom exception class
    pass


def timeout_handler(signum, frame):  # Custom signal handler
    raise TimeoutException


signal.signal(signal.SIGALRM, timeout_handler)
TIMEOUTCAP = 300


class Tester():
    def __init__(self, sort, path):
        self.sort = sort
        self.path = path
        self.output = {}

    def run_tests(self):
        list_of_folders = glob.glob(self.path + '*')
        for folder in list_of_folders:
            nr = 0
            key_name = folder.replace(self.path, '')
            self.output[key_name] = {}
            skip_run = False
            signal.alarm(TIMEOUTCAP)
            while True:
                inFile = f'{folder}/test.{nr}.in'
                outFile = f'{folder}/test.{nr}.out'

                if os.path.isfile(inFile) and os.path.isfile(outFile):
                    print(f'Test #{nr} :')
                    if not skip_run:
                        result, total_time = self.run_test(inFile, outFile)
                        if isinstance(total_time, int): assert result == True
                    else:
                        result, total_time = None, 'timeout'
                    print(f'Test result: {result}, time: {total_time} ms')
                    self.output[key_name][nr] = [total_time]
                    if result is None:
                        skip_run = True
                    nr += 1
                    continue
                break

        return self.output

    def run_test(self, inFile, outFile):
        with open(inFile, 'r') as input_file, open(outFile, 'r') as output_file:
            lines = input_file.readlines()
            n = lines[0]
            input_data = lines[1]
            input_array = [int(x) for x in input_data.strip().split(' ')]
            expect = [int(x) for x in output_file.read().strip().split(' ')]
        sort = self.sort(input_array)
        try:
            start_time = time.time() * 1000.
            sort.sort()
            total_time = round(time.time() * 1000. - start_time)
        except TimeoutException:
            print(f'{n} + {sort}: timed out after {TIMEOUTCAP} seconds')
            return None, 'timeout'
        else:
            return expect == sort.array, total_time
