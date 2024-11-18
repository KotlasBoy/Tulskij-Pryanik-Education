def is_palindrome(s):
    # Удаляем все пробелы и приводим строку к нижнему регистру
    cleaned_string = ''.join(s.split()).lower()

    # Сравниваем строку с её обратной версией
    return cleaned_string == cleaned_string[::-1]


# Должно быть напечатано True:
print(is_palindrome('А роза упала на лапу Азора'))
# Должно быть напечатано False:
print(is_palindrome('Не палиндром'))