# clock timer
from winsound import Beep
from time import sleep
import os


def main():
    users_input = int(raw_input("Enter the start time for the counter: "))
    convert_to_seconds = users_input * 60
    timer(convert_to_seconds)


def timer(tme):
    while tme:
        minutes, seconds = divmod(tme, 60)
        timeformat = '{:02d}:{:02d}'.format(minutes, seconds)
        print timeformat,
        sleep(1)
        os.system('cls')
        tme -= 1
    alarm()


def alarm():
    Freq = 2500
    Dur = 1000

    Beep(Freq, Dur)


if __name__ == '__main__':
    main()
