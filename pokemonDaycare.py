from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
maxTime = 100 # Set to maximum time allowed for script
keyHoldTime = 0.5 # Set to maximum time to change keypress
idleTime = 5

while idleTime != 0:
    if idleTime > 1:
        print(f"Starting in {idleTime} seconds")
    else:
        print(f"Starting in {idleTime} second")
    
    idleTime -= 1
    time.sleep(1)
    
idleTime = 0

try:
    print("Started")
    keyboard.press(Key.tab)
    
    while idleTime < maxTime:
        keyboard.press(Key.right)
        time.sleep(keyHoldTime)
        keyboard.release(Key.right)
        keyboard.press(Key.left)
        time.sleep(keyHoldTime)
        keyboard.release(Key.left)
        idleTime += 1
        
    keyboard.release(keys["tab"])
    print("Finished")
    
except KeyboardInterrupt:
    keyboard.release(Key.right)
    keyboard.release(Key.left)
    keyboard.release(Key.tab)
    print("Force Finish")
    
    
    
