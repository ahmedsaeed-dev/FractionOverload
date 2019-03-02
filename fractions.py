# TODO: Use try except block to input invalid input (too many forward slashes)


class InputError(Exception):
    def __init__(self, text):
        self.value = text

def menu():
    print("""
--------------------------
WELCOME TO PROJECT 2
--------------------------
A - Addition        ( + )
B - Subtraction     ( - )
C - Multiplication  ( x ) 
D - Division        ( / )
Q - Quit
    """)
    return input('Select operation: ').upper()


def get_input():
    try:
        raw_string = str(input('Enter input 1: '))
        if raw_string.count('/') != 1 or raw_string.count('/') != 0:
            raise InputError
        else:
            if '/' in raw_string:
                num, den = raw_string.split('/', 1)
                return int(num), int(den)
            else:
                return int(raw_string)
    except Exception:
        print('too many forward slashes found')
        return 'x', 'x'

def main():
    choice = ''
    while choice != 'Q':
        choice = menu()
        num, den = get_input()
        if num or den == 'x':
            print('Invalid Entry')
            continue
        print(num, den)

if __name__ == '__main__':
    main()
