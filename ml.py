import sys

from tasks import guess_number


def bulk_guess_numbers(filenames):
    for filename in filenames:
        guess_number(filename)


if __name__ == "__main__":
    bulk_guess_numbers(sys.argv[1:])
