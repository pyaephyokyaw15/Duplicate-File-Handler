# write your code here
import sys
import os


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

        file_dictionary = get_file_dictionary(root, file_format)
        for size in sorted(file_dictionary.keys(), reverse=option):
            print(f'{size} bytes')
            print(*file_dictionary[size], sep="\n")
            print()


def get_file_dictionary(root, file_format):
    file_dictionary = {}
    for (root, dirs, files) in os.walk(root, topdown=True):
        for name in files:
            extension = os.path.splitext(name)[-1].lower()

            if not file_format or extension != '.' + file_format:
                file_name = os.path.join(root, name)
                file_size = os.path.getsize(file_name)
                file_dictionary.setdefault(file_size, [])
                file_dictionary[file_size].append(file_name)

    return file_dictionary


def sorting_option():
    while True:
        sorting = int(input('Enter a sorting option:\n'))
        if sorting == 1:
            return True
        elif sorting == 2:
            return False
        print("\nWrong option\n")


if __name__ == '__main__':
    main()

