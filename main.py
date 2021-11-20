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
    sort_list = []
    for key, value in sorted(dct.items(), key=lambda x: x[1]):
        sort_list.append(key)
    return sort_list

def wtite_file(path = os.getcwd()):
    if not os.path.exists(os.path.join(path, 'result.txt')):
        file = open('result.txt', 'w')
        file.close()
    with open(os.path.join(os.getcwd(), 'result.txt'), 'wt') as file:
        for el in list_files():
            with open(os.path.join(os.getcwd(), el)) as part_file:
                for f in part_file:
                    file.write(f)
    return

wtite_file()

#проверка
with open(os.path.join(os.getcwd(), 'result.txt')) as file:
    print(file.read())

