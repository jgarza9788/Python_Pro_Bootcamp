# this will print out the Trash/Recycling Schedule
# web scrapped from the Charlotte City Website

import os,sys,re

from seleniumwire import webdriver 
from selenium.webdriver.common.by import By

DIR = os.path.dirname(os.path.realpath(__file__))

months = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']

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
    # options.add_argument('--kiosk')
    options.add_argument('log-level=3')
    # options.add_argument("user-data-dir=C:\\Users\\JGarza\\AppData\\Local\\Google\\Chrome\\User Data\\Default") 

    if visible == False:
        options.add_argument('headless')
    
    return webdriver.Chrome(executable_path=os.path.join(DIR,'chromedriver.exe'),options=options)

def clean_text(t):
    t = t.lstrip().rstrip()
    t = re.sub(r'(&nbsp;|Week|-|\.)',' ',t)
    t = re.sub(r'\s{1,100}',' ',t)
    t = re.sub(r'(<em>|</em>|\*)','',t)
    return t.split(' ')

def main():
    global months

    temp = []
    result = []

    #this is my browser 
    browser =  get_browser(False)

    #go to website 
    url = 'https://charlottenc.gov/SWS/Pages/Recycling-Collection-Schedule.aspx'
    browser.get(url)

    #find the weeks
    w = browser.find_elements(By.CLASS_NAME,'swscalpn')

    # clean each text and put it in result
    for i in w:
        temp.append(clean_text(i.get_attribute("innerHTML")))

    #find those other weeks
    w = browser.find_elements(By.CLASS_NAME,'swscalpb')

    # clean each text and put it in result
    for i in w:
        temp.append(clean_text(i.get_attribute("innerHTML")))

    # sort for days 
    temp = sorted(temp, key=lambda x: int(x[2]))

    # for for months
    for m in months:
        for t in temp:
            # print(m,t[1])
            if m == t[1]:
                result.append(t)

    #print results
    print(*result,sep='\n')




if __name__ == '__main__':
    main()