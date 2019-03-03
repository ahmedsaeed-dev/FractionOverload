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

    def check_negs(self):
        if self.num < 0 and self.den < 0:
            self.num *= -1
            self.den *= -1
        if self.den < 0:
            self.den *= -1
            self.num *= -1

    # add overload
    def __add__(self, other):
        c = Fraction()
        lcm = self.lcm(self, self.den, other.den)
        # sets common denominator
        temp_s = int(lcm / self.den)
        self.den *= temp_s
        temp_o = int(lcm / other.den)
        other.den *= temp_o
        # multiplies numerators based off common den
        self.num *= temp_s
        other.num *= temp_o

        # addition
        c.num = self.num + other.num
        c.den = self.den
        return c

    def __sub__(self, other):
        c = Fraction()
        lcm = self.lcm(self, self.den, other.den)
        # sets common denominator
        temp_s = int(lcm / self.den)
        self.den *= temp_s
        temp_o = int(lcm / other.den)
        other.den *= temp_o
        # multiplies numerators based off common den
        self.num *= temp_s
        other.num *= temp_o

        # subtraction
        c.num = self.num - other.num
        c.den = self.den
        return c

    def __mul__(self, other):
        c = Fraction()
        c.num = self.num * other.num
        c.den = self.den * other.den
        return c

    def __divmod__(self, other):
        c = Fraction()
        temp = other.num
        other.num = other.den
        other.den = temp
        return self.__mul__(other)

    @staticmethod
    def gcd(a, b):
        if a == 0 or b == 0:
            return a
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    @staticmethod
    def lcm(self, a, b):
        return (a * b) / self.gcd(a, b)

    def reduce_fractions(self):
        greatest = int(self.gcd(self.num, self.den))
        if greatest != 0:
            self.num /= greatest
            self.den /= greatest
        self.num = int(self.num)
        self.den = int(self.den)
        return

    def display_results(self):
        if self.den == 1 or self.num == 0:
            print('Results = %s' % self.num)
        else:
            print('Results = %s/%s' % (self.num, self.den))

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


def switcher(choice, c1, c2):
    if choice == 'A':
        return c1.__add__(c2)
    elif choice == 'B':
        return c1.__sub__(c2)
    elif choice == 'C':
        return c1.__mul__(c2)
    elif choice == 'D':
        return c1.__divmod__(c2)
    else:
        quits()


def main():
    # fraction 1
    f1 = Fraction()
    # fraction 2
    f2 = Fraction()
    while True:
        choice = menu()
        if choice == 'Q':
            quits()
        get_inputs(f1, 1)
        get_inputs(f2, 2)
        f1.check_negs()
        f2.check_negs()
        f3 = switcher(choice, f1, f2)
        f3.reduce_fractions()
        f3.display_results()


if __name__ == '__main__':
    main()
