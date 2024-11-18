sequence_1 = [69, 59, 57, 60, 63, 44, 46, 69]
sequence_2 = [33, 73, 50, 25, 36, 68, 52, 76]

def compare_sequences(sequence_1, sequence_2):
    if sequence_1 > sequence_2:
        return f'Список {sequence_1} больше.'
    elif sequence_1 < sequence_2:
         return f'Список {sequence_2} больше.'
    else:
        return f'Списки равны.'
        

# Вызовите функцию compare_sequences(),
# передайте в неё списки sequence_1 и sequence_2.
# Напечатайте результат, который вернёт функция.

print(compare_sequences(sequence_1, sequence_2))