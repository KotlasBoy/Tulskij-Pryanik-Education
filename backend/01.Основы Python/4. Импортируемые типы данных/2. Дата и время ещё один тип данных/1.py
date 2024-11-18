from datetime import datetime

deadline = datetime(2023, 11, 6, 9, 15, 00)
# Вместо ... напишите шаблон.
deadline_as_str = datetime.strftime(deadline, "%d.%m")
print('Ваш дедлайн:', deadline_as_str)