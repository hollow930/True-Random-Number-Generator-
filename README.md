# True-True-Random-Number-Generator-
Random Number generator in python. 

## Overview
Most python programmers are familiar with the Random module, for producing random numbers. However, these random numbers are pseudo-random numbers – which means that these values are calculated using an algorithm. It generates a sequence of numbers that are determined by an initial (seed) value.To generate true random numbers, computers need to use physical processes that are unpredictable. However, most computers do not have access to random physical processes. But I still want to create a random number generator that does not use a seed value or an algorithm, so I decided to use data that the computer can access, that changes with time in a mostly unpredictable manner. The values I used are:

-The mouse position on the screen 

-The CPU load as a percentage

-The RAM available 

-The current time in seconds 

These values are then added to an equation to spit out a number (start). To work out the random number from 0 to n, the program then calculates the remainder of division when start is divided by n. 

## Test
To test the effectiveness of the random number generator, I created a script to run the random number generator 100000 times, to work out random numbers in the range 0 to 1000. To make sure that the mouse was at different positions, I used AutoHotkey to create a script to move the mouse randomly while the program ran. Ironically, this again used some sort of pseudo-random number generator. The results shown below.

![Figure_1](https://github.com/user-attachments/assets/0fe1f089-1293-4355-8bca-4587d58e2cd6)


I ran the test program again, but this time I used the random module from python to generate numbers. As the graphs turned out very similar, giving values across the range from 1-1000, I can say that my program is effective.
![figure 2](https://github.com/user-attachments/assets/8a1662a6-4fa8-487e-8cfd-dc17dc27e33b)

## Variations
I also made another variation of this program that emulates a coin toss.

random_number.py - produces a random number bwtween 1 and n.

toin_toss.py - tosses a coin


## Instructions 
Both programs are very easy to use. However, keep in mind that you might have to download the external python modules.
External modules - 

pip install psutil

pip install pyautogui

## Limitaions 
Compared to the random module, this program is much slower, so it is not efficient if you want a large number of values.  Furthermore, as n gets very large ( more than 10 figures), there is less variation in the start value, so the numbers will not appear as random. Finally, as the mouse position plays a role in determining the start value, you might get similar results if the program is run with the mouse in the same position. 
