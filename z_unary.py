def is_relative_integer(nb):
    return isinstance(nb, int)


def is_even(nb):
    if not is_relative_integer(nb):
        raise ValueError("Le nombre doit être un entier relatif.")
    return nb % 2 == 0


def last_digit(nb):
    if not is_relative_integer(nb):
        raise ValueError("Le nombre doit être un entier relatif.")
    return abs(nb) % 10


def sum_of_digit(nb):
    if not is_relative_integer(nb):
        raise ValueError("Le nombre doit être un entier relatif.")
    return sum(int(digit) for digit in str(abs(nb)))
