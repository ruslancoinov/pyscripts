import sys
from sys import getsizeof
from time import monotonic, sleep


# Range for objects
count = 10000


def greeting(count):
    greet = ('THE ALGORITHM FOR COMPARING SET, LIST AND TUPLE FOR SPEED AND TIME',
             f'INTERVAL RANGE = {count}')
    for c in greet:
        for h in c:
            print(h, end='')
            sys.stdout.flush()
            sleep(0.04)
        print()
        if greet.index(c) == 0:
            sleep(0.5)


def main(count, foriner=count):

    my_set = set(range(1, count + 1))
    my_list = list(range(1, count + 1))
    my_tuple = tuple(range(1, count + 1))

    my_set_size = getsizeof(my_set)
    my_list_size = getsizeof(my_list)
    my_tuple_size = getsizeof(my_tuple)

    greeting(count)

    print()
    sleep(0.5)

    print(
        f'Memory size of {{set}} = {my_set_size} B = \
{round(my_set_size / 1024, 3)} KB = {round(my_set_size  / 1024 ** 2, 3)} MB')
    print(
        f'Memory size of [list] = {my_list_size} B = \
{round(my_list_size / 1024, 3)} KB = {round(my_list_size  / 1024 ** 2, 3)} MB')
    print(
        f'Memory size of (tuple) = {my_tuple_size} B = \
{round(my_tuple_size / 1024, 3)} KB = {round(my_tuple_size  / 1024 ** 2, 3)} MB')

    print()
    sleep(0.8)

    start = monotonic()  # start variable keeps process start time
    for i in range(foriner):
        if i in my_set:
            pass
    # timein' again and subtract start - it shows process uptime.
    print(f'Set uptime = {round(monotonic() - start, 3)} sec')
    my_set.clear()  # Freed some memory

    start = monotonic()
    for i in range(foriner):
        if i in my_list:
            pass
    print(f'List uptime = {round(monotonic() - start, 3)} sec')
    my_list.clear()

    start = monotonic()
    for i in range(foriner):
        if i in my_tuple:
            pass
    print(f'Tuple uptime = {round(monotonic() - start, 3)} sec')


if __name__ == '__main__':
    main(count)
