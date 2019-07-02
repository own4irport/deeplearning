import time
import threading


def go_home():
    for i in range(10):
        print("gohomeing......")
        time.sleep(1)


def buy_icecream():
    for i in range(10):
        print("goschool......")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=go_home)
    t2 = threading.Thread(target=buy_icecream)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        print(len(threading.enumerate()))
        if len(threading.enumerate()) < 2:
            break
        time.sleep(1)


if __name__ == '__main__':
    main()
