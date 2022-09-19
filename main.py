from converter import dec_to_bin


def say_hello():
    print("Hello")


if __name__ == '__main__':
    print(*dec_to_bin(256))
