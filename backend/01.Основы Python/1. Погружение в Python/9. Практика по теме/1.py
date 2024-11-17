bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34
list_of_lang = [bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql]
def analyze_skills():
    # Среди всех переменных найдите минимальное и максимальное значение.
    # Напечатайте фразы, описанные в задании (две строки).
    print(f'Доля питонистов, у которых есть наименее популярный навык (в %): {min(list_of_lang)}')
    print(f'Доля питонистов, у которых есть наиболее популярный навык (в %): {max(list_of_lang)}')

# Не удаляйте вызов функции.
analyze_skills()