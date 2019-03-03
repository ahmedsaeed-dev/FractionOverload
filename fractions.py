# TODO: create overload add for both user objects


class InvalidInputError(Exception):
    def __init__(self, text):
        self.value = text


class Fraction:
    def __init__(self):
        self.improper_whole = 1
        self.num = 0
        self.den = 1
        self.raw_string = ''
        self.input_list = []

    # add overload
    def __add__(self, other):
        c3 = Fraction()
        lcm = self.lcm(self.den, other.den)
        # sets common denominator
        temp_s = int(lcm / self.den)
        self.den *= temp_s
        temp_o = int(lcm / other.den)
        other.den *= temp_o
        # multiplies numerators based off common den
        self.num *= temp_s
        other.num *= temp_o
        c3.num = self.num + other.num
        c3.den = self.den
        return c3

    @staticmethod
    def lcm(a, b):
        x, y = a, b
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return (x * y) / a

    def get_input(self, i):
        try:
            self.raw_string = str(input('Enter input %d: ' % i))
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
                        self.input_list = self.num, self.den
                        return
                    # if pure fraction
                    else:
                        self.num, self.den = self.raw_string.split('/', 1)
                        self.input_list = int(self.num), int(self.den)
                        return
                else:
                    self.input_list = int(self.raw_string), 1
                    return
        except Exception:
            print('Invalid input. Please try again.')
            self.input_list = 'e'


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


def quits():
    print("\n----------------\n   THANKS!\n----------------")
    exit(0)


def get_inputs(c, i):
    while True:
        c.get_input(i)
        if c.input_list[0] == 'e':
            continue
        else:
            break
    c.num, c.den = c.input_list


def addition(c1, c2):
    return c1.__add__(c2)


def switcher(choice, c1, c2):
    if choice == 'A':
        return addition(c1, c2)
    elif choice == 'B':
        pass
    elif choice == 'C':
        pass
    elif choice == 'D':
        pass
    else:
        quits()


def display_output(c):
    print('Results = %s/%s' % (c.num, c.den))



def main():
    # fraction 1
    f1 = Fraction()
    # fraction 2
    f2 = Fraction()
    # new fraction
    f3 = Fraction()
    while True:
        choice = menu()
        if choice == 'Q':
            quits()
        get_inputs(f1, 1)
        get_inputs(f2, 2)
        f3 = switcher(choice, f1, f2)
        display_output(f3)


if __name__ == '__main__':
    main()
