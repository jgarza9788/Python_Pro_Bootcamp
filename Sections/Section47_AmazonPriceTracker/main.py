from lib2to3.pgen2.token import LESS
import os, sys
from bs4 import BeautifulSoup as bs
import requests

# import yagmail 


def main(data):
    # get price
    url = data['AmazonURL']
    page = requests.get(url, headers={"Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"})
    soup = bs(page.text, "html.parser")
    p0 = soup.findAll("span", attrs={"class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})[0]
    p1 = p0.findAll("span", attrs={"class": "a-offscreen"})[0]
    print(p1.text)

    price = float(p1.text.replace('$',''))
    print('the price is {}'.format(price))

    """
    if error sending email:
        https://www.google.com/settings/security/lesssecureapps
    use TWILIO or automate it with Selenium
    """
    # if price <= data['less_than_price']:
        # yagmail.register(data['email'], data['password'])
        # yag = yagmail.SMTP(data['email'])
        # contents = 'the price is below {less_than_price} \n {url}'.format(
        #     less_than_price=data['less_than_price'],
        #     url=data['AmazonURL'])
        # yag.send(data['email'], subject = "price alert", contents = contents)





if __name__ == '__main__':
    import Config
    config = Config.Config()
    # print(config.data)
    
    main(config.data)