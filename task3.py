# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок
def exclude(txt:str,string_to_del:str):
    result=(list(filter(lambda x: string_to_del not in x ,list(txt.split(' ')))))
    return result

input_text=input('Введите текст для обработки: ')
needed_string=input('Введите строку, которую будем удалять из текста: ')
result_text=exclude(input_text,needed_string)
print('Текст после обработки: '," ".join(result_text))