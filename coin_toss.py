import psutil
import pyautogui
import time


def toss_coin():

    x,y = pyautogui.position()
    cpu= psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory().available
    current_time_s = time.time()
    
    start = int (((x*memory+current_time_s )) +(3*cpu)+(5*cpu) +y)

    if start % 2 == 0:
        print('HEADS')

    else:
        print('TAILS')

def main():
    toss_coin()


if __name__ == "__main__":
    main()
