import os
# вариант для небольшого размера файлов
# def count_str(path_file):
#     with open(path_file) as file:
#         s = file.readlines()
#         return len(s)

def count_str(path_file):
    with open(path_file) as file:
        count = 0
        for f in file:
            count += 1
    return count

def list_files(path_dir=os.getcwd()):
    files = os.listdir(path=path_dir)
    dct = {}
    for f in files:
        if f.endswith('.txt') and f != 'result.txt':
            path = os.path.join(os.getcwd(), f)
            dct[f] = count_str(path)
    sort_dct = {}
    for key, value in sorted(dct.items(), key=lambda x: x[1]):
        sort_dct[key] = value
    return sort_dct

def wtite_file(path = os.getcwd()):
    with open(os.path.join(os.getcwd(), 'result.txt'), 'wt') as file:
        dct = list_files()
        for el in dct:
            with open(os.path.join(os.getcwd(), el)) as part_file:
                file.write(f'Файл {el} \n')
                file.write(str(dct[el]) + '\n')
                for f in part_file:
                    file.write(f)
                file.write('\n')
    return

wtite_file()

#проверка
with open(os.path.join(os.getcwd(), 'result.txt')) as file:
    print(file.read())