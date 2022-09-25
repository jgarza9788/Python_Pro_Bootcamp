
import sys
import os
import time
import Config

from seleniumwire import webdriver 
from selenium.webdriver.common.by import By

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
    # options.add_argument('--kiosk')
    options.add_argument('log-level=3')
    # options.add_argument("user-data-dir=C:\\Users\\JGarza\\AppData\\Local\\Google\\Chrome\\User Data\\Default") 

    if visible == False:
        options.add_argument('headless')
    
    return webdriver.Chrome(executable_path=os.path.join(DIR,'chromedriver.exe'),options=options)

def signin(browser, config_data):
    browser.get('https://www.linkedin.com/login')

    userNameField = browser.find_element_by_css_selector('input[name=session_key]')
    passwordField = browser.find_element_by_css_selector('input[name=session_password]')
    signinButton = browser.find_element_by_css_selector('button[type=submit]')

    userNameField.send_keys(config_data['email']) 
    passwordField.send_keys(config_data['password']) 
    signinButton.click()

    return browser

def goto_jobs(browser,keywords=None,location=None,Onsite=True,Remote=True,Hybrid=True):
    url = 'https://www.linkedin.com/jobs/collections/?f_AL=true' #easy apply by default

    if keywords != None:
        url += '&keywords=' + keywords

    if location != None:
        url += '&location=' + location.replace(' ','%20').replace(',','%2C')
    
    if Onsite or Remote or Hybrid:
        url += '&f_WT='
        if Onsite:
            url += '1'
            url += '%2C'
        if Remote:
            url += '2'
            url += '%2C'
        if Hybrid:
            url += '3'
    
    browser.get(url)
    return browser

def apply_to_all(browser):

    jobs = browser.find_elements_by_xpath('/html/body/div[6]/div[3]/div[4]/div/div/main/div/section[1]/div/ul/li[*]')

    print(len(jobs),' jobs ')

    submitted_app_count = 0 

    for j in jobs:
        j.click()
        print('starting in 3 seconds')
        time.sleep(3)


        applybutton = None
        try_count = 0 
        while applybutton == None and try_count < 10:
            try:
                applybutton = browser.find_element_by_xpath('/html/body/div[6]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/div/div/button/span')
            except:
                pass
            time.sleep(1)
            try_count += 1
        
        try:
            applybutton.click()
        except:
            continue
        

        print('try the next button 10 times')
        for i in range(10):
            time.sleep(1)
            try:
                nb = browser.find_element_by_css_selector('button[aria-label="Continue to next step"]')
                nb.click()
            except:
                pass

        print('review the application')
        try:
            time.sleep(1)
            nb = browser.find_element_by_css_selector('button[aria-label="Review your application"]')
            nb.click()
        except:
            pass

        print('submit the application')
        try:
            time.sleep(1)
            nb = browser.find_element_by_css_selector('button[aria-label="Submit application"]')
            nb.click()
            submitted_app_count += 1
            print('submitted_app_count: ',submitted_app_count)
        except:
            pass

        print('exit the window thingie')
        try:
            time.sleep(1)
            exitbutton = browser.find_element_by_css_selector('button[aria-label="Dismiss"]')
            exitbutton.click()
            time.sleep(1)

            discardbutton = browser.find_element_by_css_selector('button[data-control-name="discard_application_confirm_btn"]')
            discardbutton.click()
        except:
            pass
        


    return submitted_app_count





def main():
    config = Config.Config()
    cd = config.data
    # print(cd)

    browser = get_browser()
    signin(browser, cd)

    # convert site types to boolean
    Onsite = cd['Onsite'] == 'True'
    Remote = cd['Remote'] == 'True'
    Hybrid = cd['Hybrid'] == 'True'

    goto_jobs(browser,cd['search'],cd['location'],Onsite,Remote,Hybrid)
    count = apply_to_all(browser)

    #result 
    print('applied to ',count, ' jobs')


if __name__ == '__main__':
    main()