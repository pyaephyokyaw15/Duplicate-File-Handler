import sys
import os
from collections import defaultdict
import hashlib


def main():
    if len(sys.argv) < 2:
        print('Directory is not specified')

    else:
        root = sys.argv[1]
        file_format = input('Enter file format:\n')
        print('\nSize sorting options:')
        print('1. Descending')
        print('2. Ascending')
        option = sorting_option()
        print()

        size_map = get_size_map(root, file_format)

        for size in sorted(size_map, reverse=option):
            print(f'{size} bytes')
            print(*size_map[size], sep="\n")
            print()

        if check_duplicate_flag():
            number = 1
            hash_table_map = get_hash_table_map(size_map, option)
            duplicate_files = []
            for size, hash_table in hash_table_map.items():
                print(f'{size} bytes')
                for hash_value, files in hash_table.items():
                    if len(files) > 1:
                        print(f'Hash: {hash_value}')
                        for file in files:
                            print(f'{number}. {file}')
                            number += 1
                            duplicate_files.append((file, size))
                print()

        if delete_flag():
            delete_files(duplicate_files)


def check_duplicate_flag():
    while True:
        sorting = input('Check for duplicates?\n')
        print()
        if sorting == 'yes':
            return True
        elif sorting == 'no':
            return False
        print("\nWrong option\n")



def get_size_map(root, file_format):
    # size_map = {}
    size_map = defaultdict(list)
    for (root, dirs, files) in os.walk(root, topdown=True):
        for name in files:
            extension = os.path.splitext(name)[-1].lower()

            if not file_format or extension == '.' + file_format:
                file_name = os.path.join(root, name)
                file_size = os.path.getsize(file_name)
                # size_map.setdefault(file_size, [])
                size_map[file_size].append(file_name)

    return size_map


def sorting_option():
    while True:
        sorting = int(input('Enter a sorting option:\n'))
        if sorting == 1:
            return True
        elif sorting == 2:
            return False
        print("\nWrong option\n")


def delete_files(dupliacte_files):
    while True:
        print()
        user_input = input('Enter file numbers to delete:\n')
        print()

        if not user_input:
            print()
            print('Wrong format')
            print()
            continue


        numbers = user_input.split()
        free_space = 0
        try:
            numbers = [int(number) for number in numbers]
            if all(number <= len(dupliacte_files) for number in numbers):
                for number in numbers:

                    os.remove(dupliacte_files[number-1][0])
                    print(dupliacte_files[number-1][0])
                    free_space += dupliacte_files[number-1][1]

                print()
                print(f'Total freed up space: {free_space} bytes')

                break

            else:
                print()
                print('Wrong format')
                print()


        except:
            print()
            print('Wrong format')
            print()







# https://stackoverflow.com/questions/18724376/finding-duplicate-files-via-hashlib
def get_file_hashMD5(filename):
    m = hashlib.md5()
    with open(filename, 'rb', 1024 * 1024) as fh:
        while True:
            data = fh.read(1024 * 1024)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def get_hash_table_map(size_map, option):
    hash_table_map = {}
    for size in sorted(size_map, reverse=option):

        if len(size_map[size]) > 1:
            hash_table = defaultdict(list)
            for file in size_map[size]:
                hash_table[get_file_hashMD5(file)].append(file)

            hash_table_map[size] = hash_table

    return hash_table_map


def delete_flag():
    while True:
        print()
        check = input('Delete Files?\n')
        print()

        if check == 'yes':
            return True
        elif check == 'no':
            return False




if __name__ == '__main__':
    main()
