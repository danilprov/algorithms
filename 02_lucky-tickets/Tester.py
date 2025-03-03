import os


class Tester():
    def __init__(self, task, path):
        self.task = task
        self.path = path

    def run_tests(self):
        nr = 0
        while True:
            inFile = f'{self.path}test.{nr}.in'
            outFile = f'{self.path}test.{nr}.out'

            if os.path.isfile(inFile) and os.path.isfile(outFile):
                print(f'Test #{nr} :')
                print(f'Test result: {self.run_test(inFile, outFile)}')
                nr += 1
                continue
            break

    def run_test(self, inFile, outFile):
        with open(inFile, 'r') as input_file, open(outFile, 'r') as output_file:
            input_data = input_file.read().strip()
            expect = output_file.read().strip()
        actual = self.task.run(input_data)
        print(f'n: {input_data}, # lucky tickets: {actual}')
        return expect == actual
