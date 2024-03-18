import string
import random
import pyuac
# import os
import subprocess
import time
import pyautogui


def main():
    setup_path = r'd:/setup.exe'
    subprocess.Popen([setup_path])
    time.sleep(18)
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.press('left')
    time.sleep(1)
    pyautogui.moveTo(1150, 840)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(15)
    pyautogui.write('DTV-08641')
    time.sleep(1)
    pyautogui.moveTo(1150, 840)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.press('left')
    time.sleep(1)
    pyautogui.moveTo(1150, 840)
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(840, 390)
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.moveTo(890, 390)
    pyautogui.click(button='left')
    time.sleep(1)

    for t in range(100):
        pyautogui.moveTo(960, 390)
    #    pyautogui.click(button='left')
        pyautogui.doubleClick(button='left')
#        pyautogui.press('backspace')
        time.sleep(0.01)
#        for _ in range(5):
        for _ in range(1):
            pyautogui.press('backspace')
        time.sleep(0.01)
        pyautogui.doubleClick(button='left')
        pyautogui.press('backspace')

        letters = string.ascii_uppercase
        digits = string.digits
        key = ''.join(random.choices(letters, k=3)) + '-' + \
            ''.join(random.choices(digits, k=5))
        pyautogui.typewrite(key)
        time.sleep(0.01)
        pyautogui.moveTo(1150, 840)
        pyautogui.click(button='left')
   #     time.sleep(1)
        pyautogui.moveTo(1150, 640)
        pyautogui.click(button='left')
    #    time.sleep(1)
        with open("test.txt", "a") as myfile:
            myfile.write(f'{key} \n')
        
        myfile.close()
        t += 1


if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()  # Already an admin here.
