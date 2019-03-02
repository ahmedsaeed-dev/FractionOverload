# TODO: allow main to instantiate second input as member of class User
# TODO: create overload add for both user objects

class InvalidInputError(Exception):
    def __init__(self, text):
        self.value = text


class User:
    def __init__(self):
        self.improper_whole = 1
        self.num = 0
        self.den = 1
        self.choice = ''
        self.raw_string = ''

    def get_input(self):
        try:
            self.raw_string = str(input('Enter input 1: '))
            if self.raw_string.count('/') > 1:
                raise InvalidInputError
            else:
                # if input is a fraction
                if '/' in self.raw_string:
                    # if input is an mixed fraction, return as improper
                    if ' ' in self.raw_string:
                        self.improper_whole, self.raw_string = self.raw_string.split(' ')
                        self.num, self.den = self.raw_string.split('/', 1)
                        self.improper_whole = int(self.improper_whole)
                        self.num = int(self.num)
                        self.den = int(self.den)
                        self.num = self.improper_whole * self.den + self.num
                        return self.num, self.den
                    # if pure fraction
                    else:
                        self.num, self.den = self.raw_string.split('/', 1)
                        return int(self.num), int(self.den)
                else:
                    return int(self.raw_string), 1
        except Exception:
            print('Invalid input. Please try again.')
            return 'e'

    @staticmethod
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


def main():
    user = User()
    while True:
        user.choice = user.menu()
        if user.choice == 'Q':
            print("""
--------------------------
    THANK YOU - GOODBYE
--------------------------
            """)
            exit(0)
        input_list = user.get_input()
        if input_list[0] == 'e':
            continue
        else:
            user.num, user.den = input_list

        print('Fraction: %s/%s' % (user.num, user.den))


if __name__ == '__main__':
    main()
