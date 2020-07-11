import os

path = 'C:'
filename = 'Adobe'
result = []


def find_file():
    i = 0
    for root, lists, files in os.walk(path):
        for file in files:
            if filename in file:
                i = i + 1
                write = os.path.join(root, file)
                print('%d %s' % (i, write))
                result.append(write)


def find_file_and_putin_txt():
    i = 0
    open('E:\Python\\find_file.txt', mode='w').close()
    for root, lists, files in os.walk(path):
        for file in files:
            if filename in file:
                i = i + 1
                write = os.path.join(root, file)

                file_txt = open('E:\Python\\find_file.txt', mode='a+')
                file_txt.write('%d %s \n' % (i, write))
                result.append(write)


if __name__ == '__main__':
    find_file()
    find_file_and_putin_txt()
