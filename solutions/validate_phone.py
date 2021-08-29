import re

def validate_phone(numbers):

    pattern = re.compile(r'^[7-9]\d{9}$')

    for number in numbers:
        if pattern.match(number):
            print('YES')
        else:
            print('NO')