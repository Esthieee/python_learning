from datetime import datetime
import time
import random

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for i in range(3):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute")
    wait_time = random.randint(1, 30)
    time.sleep(wait_time)

today = datetime.today().strftime("%A")
if today == 'Saturday':
    print('Party')
elif today == 'Sunday':
        print('Rest.')
else:
    print('Work, work, work.')

for i in "sleep":
    print(i)

for num in range(3):
    print('Hello, there!')

word = "bottles"
for beer_num in range(12, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word , "of beer on the wall.")
    print()
    
