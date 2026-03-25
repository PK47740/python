import pyautogui
import time

# Wait 5 seconds so you can prepare
time.sleep(5)

# Find the COC icon on screen
location = pyautogui.locateOnScreen("coc.jpeg", confidence=0.8)

if location is not None:
    # Get center of the icon
    center = pyautogui.center(location)
    
    # Move mouse and click
    pyautogui.moveTo(center.x, center.y, duration=1)
    pyautogui.click()
    
    print("COC clicked successfully!")
else:
    print("COC icon not found!")