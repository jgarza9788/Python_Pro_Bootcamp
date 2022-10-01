
import sys
import os
import time
import Config

from seleniumwire import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

DIR = os.path.dirname(os.path.realpath(__file__))

def get_browser(visible= True):
    #options
    options = webdriver.ChromeOptions()
    # options.add_argument('test-type')
    # options.add_argument("--no-sandbox") # no sandboxing
    # chrome_options.add_argument("--load-extension=" + unpackedExtensionPath)
    # options.add_argument('--js-flags=--expose-gc')
    # options.add_argument('--enable-precise-memory-info')
    # options.add_argument('--disable-popups-blocking')
    # options.add_argument('--disable-default-apps')
    # options.add_argument('test-type=browser')
    # options.add_argument('disable-infobars')
    # options.add_argument('window-size=800x600')
    # options.add_argument('window-size=1600x1200')
    options.add_argument('start-maximized')
    # options.add_argument('--kiosk')
    # options.add_argument('log-level=3')
    # options.add_argument("user-data-dir=C:\\Users\\JGarza\\AppData\\Local\\Google\\Chrome\\User Data\\Default") 

    if visible == False:
        options.add_argument('headless')
    
    return webdriver.Chrome(executable_path=os.path.join(DIR,'chromedriver.exe'),options=options  )

def signin(browser, config_data):
    browser.get('https://tinder.com/')

    # time.sleep(5)

    # loginbutton = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
    loginbutton = browser.find_element_by_css_selector('a[class="c1p6lbu0 Miw(120px)"]')
    loginbutton.click()

    time.sleep(10)

    facebookbutton = browser.find_element_by_css_selector('button[aria-label="Log in with Facebook"]')
    facebookbutton.click()

    time.sleep(10)
    # print(*browser.window_handles)
    # time.sleep(10)

    browser.switch_to.window(browser.window_handles[1])
    print(browser.title)

    userNameField = browser.find_element_by_css_selector('input[id="email"]')
    passwordField = browser.find_element_by_css_selector('input[id="pass"]')
    signinButton = browser.find_element_by_css_selector('input[type="submit"]')

    userNameField.send_keys(config_data['email']) 
    passwordField.send_keys(config_data['password']) 
    signinButton.click()

    time.sleep(10)

    browser.switch_to.window(browser.window_handles[0])
    print(browser.title)

    try:
        allowButton = browser.find_element_by_css_selector('button[aria-label="Allow"]')
        allowButton.click()
    except:
        pass

    time.sleep(10)

    try:
        enableButton = browser.find_element_by_css_selector('button[aria-label="Enable"]')
        enableButton.click()
    except:
        pass

    time.sleep(10)

    try:
        acceptButton = browser.find_element_by_css_selector('button[class="c1p6lbu0 W(100%) W(a)--ml Mx(4px)--ml My(0)--ml"]')
        acceptButton.click()
    except:
        pass

    time.sleep(10)


    # time.sleep(500)

    return browser

def like(browser,times=100):

    # main = browser.find_element_by_css_selector('main[class="H(100%) Ov(h) Pos(r) Bgc($c-ds-background-secondary) Z(1) Fx($flx1) BdStart Bdc($c-ds-divider-primary)"]')

    for i in range(times):
        # print(Keys.RIGHT)
        # print(Keys.ARROW_RIGHT)
        # main.send_keys(Keys.RIGHT)
        try:
            likeButton = browser.find_element_by_css_selector('button[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgi($g-ds-background-like):a"]')
            likeButton.click()
        
        except ElementClickInterceptedException:
            try:
                match_popup = browser.find_element_by_css_selector(".itsAMatch a")
                match_popup.click()
            except NoSuchElementException:

                try:
                    tindergold = browser.find_element_by_css_selector('button[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) C($c-ds-text-secondary) C($c-ds-text-primary):h Fw($semibold) focus-button-style D(b) My(20px) Mx(a)"]')
                    tindergold.click()
                except:
                    pass

                try:
                    tinderplus = browser.find_element_by_css_selector('button[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(42px)--s Mih(50px)--ml Pos(r) Ov(h) C(#fff) Bg($c-pink):h::b Bg($c-pink):f::b Bg($c-pink):a::b Trsdu($fast) Trsp($background) Bg($g-ds-background-brand-gradient) button--primary-shadow StyledButton Bxsh($bxsh-btn) Fw($semibold) focus-button-style My(20px)--ml Mb(10px)--s W(100%)"]')
                    tinderplus.click()
                except:
                    pass

        time.sleep(1)



def main():
    config = Config.Config()
    cd = config.data
    # print(cd)

    browser = get_browser()
    signin(browser, cd)

    like(browser,100)


if __name__ == '__main__':
    main()