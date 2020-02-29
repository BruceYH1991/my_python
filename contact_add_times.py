

import fileinput


def main():
    member_times = read_times('r.txt')
    add_times('result.txt', member_times)
    add_times('result.txt.1', member_times)
    add_times('result.txt.2', member_times)


def read_times(path):
    result = {}
    with fileinput.input(path) as files:
        for file in files:
            member_id, times = file.replace('\n', '').replace(' ', '').split(',')
            result[member_id] = times
    return result


def add_times(path, member_times):
    with fileinput.input(path, inplace=True, backup='.o') as files:
        for file in files:
            v, a, m1, m2, r = file.replace('\n', '').replace(' ', '').split(',')
            file = file.replace('\n', '') + ',' + member_times.get(m2, '0')
            print(file)


if __name__ == '__main__':
    main()













