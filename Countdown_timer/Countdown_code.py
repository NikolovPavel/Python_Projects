import time
t = int(input('Enter the time in seconds: '))


def countdown(t):
    while t:
        hours = int(t / 3600)
        minutes = int(t / 60) % 60
        seconds = t % 60
        timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
        print(timer)
        time.sleep(1)
        t -= 1
    print('Boom!')
    exit()


print(countdown(t))
