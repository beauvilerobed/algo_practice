from operator import contains
import os
import glob


def generate_files(path='/tests/*'):
    file_path = os.getcwd() + path

    paths = glob.glob(file_path)
    input_files = []
    output_files = []

    for path in paths:
        if 'input' in path:
            input_files.append(path)
        elif 'output' in path:
            output_files.append(path)

    input_files.sort()
    print('number of input files is {}'.format(len(input_files)))
    output_files.sort()
    print('number of output files is {}'.format(len(output_files)))

    return input_files, output_files


def generate_cases(input_files, output_files):
    cases = []
    for name1, name2 in zip(input_files, output_files):
        with open(name1, 'r') as f:
            lines = f.readlines()
            case = list(map(int, lines))

        with open(name2, 'r') as f:
            line = f.readline()
            data = int(line)

        cases.append([case, data])
        print("finished processing file", len(cases))

    return cases
