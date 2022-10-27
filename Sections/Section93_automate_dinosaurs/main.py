# requires python 3.8 or less
# check compatibility --> https://pypi.org/project/PyAutoGUI/#description
#!conda activate py38  

import os,time
import pyautogui
import keyboard

from selenium import webdriver

from highscore_manager import highscore_manager as HSM
hsm = HSM()

DIR = os.path.dirname(os.path.realpath(__file__))

def get_browser(visible= True):
    #options
    options = webdriver.ChromeOptions()
    options.add_argument('test-type')
    # options.add_argument("--no-sandbox") # no sandboxing
    # chrome_options.add_argument("--load-extension=" + unpackedExtensionPath)
    options.add_argument('--js-flags=--expose-gc')
    options.add_argument('--enable-precise-memory-info')
    options.add_argument('--disable-popups-blocking')
    options.add_argument('--disable-default-apps')
    options.add_argument('test-type=browser')
    options.add_argument('disable-infobars')
    # options.add_argument('window-size=800x600')
    # options.add_argument('window-size=1600x1200')
    options.add_argument('start-maximized')
    options.add_argument('log-level=3')
    # options.add_argument("user-data-dir=C:\\Users\\JGarza\\AppData\\Local\\Google\\Chrome\\User Data\\Default") 

    if visible == False:
        options.add_argument('headless')
    
    return webdriver.Chrome(executable_path=os.path.join(DIR,'chromedriver.exe'),options=options)


browser =  get_browser(True)
browser.get('https://googledino.com/')
# full screen
pyautogui.getWindowsWithTitle("Google Dinosaur Game - Google Chrome")[0].maximize()



XYs = [
    [1620,720],
    [1619,720],
    [1618,720],
    [1617,720],
    [1616,720],
    [1615,720],

    [1620,718],
    [1619,718],
    [1618,718],
    [1617,718],
    [1616,718],
    [1615,718],

    [1620,715],
    [1619,715],
    [1618,715],
    [1617,715],
    [1616,715],
    [1615,715],
    ]

#R=83 G=83 B=83 

pyautogui.keyDown('space')

score = 0 

while 1:
    
    for xy in XYs:
        if pyautogui.pixel(xy[0],xy[1])==(83,83,83):  
            print(xy[0],xy[1],'jump!')
            pyautogui.keyDown('space')
            time.sleep(0.0001)
            pyautogui.keyUp('space')
            score += 1
            # break

    if pyautogui.pixel(1971,646)==(83,83,83):  
        print('💀 -> 🔁')
        print(score,hsm.data['score'])
        if score > hsm.data['score']:
            hsm.data['score'] = score
            hsm.save()
        score = 0  


        pyautogui.press('return')

    if keyboard.is_pressed('esc')==True:
        print('end program')
        break     

