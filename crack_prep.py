import string
import random
import pyuac
import subprocess
import time
import pyautogui


def main():
    '''Navigation & keygen function.

    This function performs pyatogui lib navigation through the installation software,
    scroll pages, click on certain point of x-y screen cords and 
    generates sudden LLL-FFFFF code, related to the sections of the software.
    It also write file with all keygen attempts.'''
    setup_path = r'e:/setup.exe'
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


    for t in range(100000):
        pyautogui.moveTo(960, 390)
        pyautogui.doubleClick(button='left')   
        for _ in range(5):
            pyautogui.press('backspace')

        letters = string.ascii_uppercase
        digits = string.digits
        key = ''.join(random.choices(letters, k=3)) + '-' + \
            ''.join(random.choices(digits, k=5))
        pyautogui.typewrite(key)
        pyautogui.moveTo(1150, 840)
        pyautogui.click(button='left')
        pyautogui.moveTo(1150, 640)
        pyautogui.click(button='left')
        with open("test.txt", "a") as myfile:
            myfile.write(f'{key} \n')
        
        myfile.close()
        t += 1


if __name__ == "__main__":
    '''This is for uprun within admin rights.'''
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:
        main()
