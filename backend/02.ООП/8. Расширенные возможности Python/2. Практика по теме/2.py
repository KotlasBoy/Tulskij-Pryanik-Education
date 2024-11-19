def obfuscator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if 'name' in result and 'password' in result:
            name = result['name']
            password = result['password']

            if len(name) > 2:
                obfuscated_name = name[0] + '*' * (len(name) - 2) + name[-1]
            else:
                obfuscated_name = name

            obfuscated_password = '*' * len(password)

            result['name'] = obfuscated_name
            result['password'] = obfuscated_password

        return result
    return wrapper

@obfuscator
def get_credentials():
    return {
        'name': 'StasBasov',
        'password': 'iamthebest'
    }


print(get_credentials())