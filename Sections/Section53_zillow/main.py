# not working due to Zillow blocking Bots



import sys
import os
import time
import Config

from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver

DIR = os.path.dirname(os.path.realpath(__file__))

def get_all_zillow_data(config_data):

    response = requests.get(config_data['zillow_url'], headers=config_data['zillow_header'])
    print(response.text)

    s = bs(response.text,"html.parser")

    all_links = []

    for links in s.select('.property-card-link a'):
        href = links["href"]
        print(href)
        if "http" not in href:
            all_links.append(f"https://www.zillow.com{href}")
        else:
            all_links.append(href)

    all_address_elements = s.select("address")
    all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

    all_price_elements = s.select("span")
    all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]

    return all_links, all_addresses, all_prices


# def get_all_zillow_data2(browser,config_data):

#     time.sleep(3)

#     browser.get(config_data['zillow_url'])

#     boxes = browser.find_elements_by_xpath('/html/body/div[1]/div[5]/div/div/div/div[1]/ul/li[*]')
#     for b in boxes:
#         print(b.get_attribute('innerHTML'))


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

# def signin(browser, config_data):
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


def fill_in_form(browser,config_data,l,a,p):

    for i,_ in enumerate(l):
        browser.get(config_data['google_form_url'])
        
        time.sleep(2)
        link = browser.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address = browser.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price = browser.find_element_by_xpath(
            '/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_button = browser.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

        address.send_keys(a[i])
        price.send_keys(p[i])
        link.send_keys(l[i])
        submit_button.click()



def main():
    config = Config.Config()
    cd = config.data
    
    # browser = get_browser()
    l,a,p = get_all_zillow_data(cd)
    for i in range(len(l)):
        try:
            print(l[i])
        except:
            pass
        try:
            print(a[i])
        except:
            pass
        try:
            print(p[i])
        except:
            pass


    # fill_in_form(browser,cd,l,a,p)



if __name__ == '__main__':
    main()