import sys
import time
import pyprind


n = 100
sleeptime = 0.05


def test_bar():
    bar = pyprind.ProgBar(n, bar_char='#')
    for i in range(n):
        time.sleep(sleeptime)
        bar.update()


if __name__ == '__main__':

    print('Basic Progress Bar\n')
    test_bar()
