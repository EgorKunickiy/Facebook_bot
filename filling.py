import random


def text() -> str:
    t = list(map(chr, [random.randint(97, 122) for _ in range(5)]))
    return ''.join(t)


def number() -> str:
    return str(random.randint(1, 28))


def date() -> str:
    return str(random.randint(1990, 1999))


if __name__ == '__main__':
    print(text())
    print(number())
    print(date())
