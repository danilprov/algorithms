import numpy as np
import os


def generate_array(size, input='random'):
    if input == 'random':
        return np.random.randint(0, size, size)
    elif input == 'three-digit':
        return np.random.randint(0, 999, size)


def write_to_file(i, array, path='resources/'):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + f'test.{i}.in', 'w') as file:
        file.write(str(10**i) + '\n')
        file.write(' '.join(map(str, array)))

    expected = sorted(array)
    with open(path +f'test.{i}.out', 'w') as file:
        file.write(' '.join(map(str, expected)))


np.random.seed(1)
for j, input_type in enumerate(['random', 'three-digit']):
    path = 'resources/' + str(j) + '.' + input_type + '/'
    for i in range(8):
        array = generate_array(10**i, input_type)
        write_to_file(i, array, path)
