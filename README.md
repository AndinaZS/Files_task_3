# Домашнее задание к лекции: Задача 3
# тема: «Открытие и чтение файла, запись в файл»
### *Основная функция wtite_file()*
На вход получет путь к директории с файлами. По умолчанию - текущий каталог. 
Функция перезаписывет файл 'result.txt' текстом из файлов в соответствии с условием задачи.
Функция проверяет существование файла 'result.txt', при необходимости сосздает его в текущем каталоге. 

### *Функция list_files()*
На вход получет путь к директории с файлами. По умолчанию - текущий каталог.
Формирует словаь, содержащий имена фалов, как ключи и количество строк в фале (подсчет в функции count_str()). По реализованной логике использует все текстовые файлы в каталоге, кроме 'result.txt'.
На основе полученного словаря создается новый словарь с отсортированными по значеним элеметами.


### *Функция count_str()*
На вход олучает путь к файлу и возвращает количество строк в файле.
