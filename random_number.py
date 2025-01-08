import psutil
import pyautogui
import time


def random_number(upper):

    x,y = pyautogui.position()
    cpu= psutil.cpu_percent(interval=0.1)
    memory = psutil.virtual_memory().available
    current_time_s = time.time()
    
    
    start = int (((x*memory+current_time_s )) +(3*cpu)+(5*cpu) +y)
    

    return int(start % (upper+1) )


def main():

    userInput = int(input("Find random number between 0 and n \n Enter n: "))
    print(f"Random Number - {random_number(userInput)}")


if __name__ == "__main__":
    main()
