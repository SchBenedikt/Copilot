import pyautogui 
import time

def run_code():
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.typewrite("microsoft-edge://?ux=copilot&tcp=1&source=taskbar")
    pyautogui.press("enter")

run_code()
