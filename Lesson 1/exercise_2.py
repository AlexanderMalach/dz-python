import time


def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(sec))
sec = int(input('Введите время в секундах '))

print(convert(sec))


