countdown_str = ''

for i in reversed(range(11)):
    countdown_str = countdown_str + str(i) + ', '

countdown_str = countdown_str + 'поехали!'

print(countdown_str)