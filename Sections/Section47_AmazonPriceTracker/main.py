
import os, sys
from bs4 import BeautifulSoup as bs
import requests

from email.message import EmailMessage
import ssl
import smtplib

def main(data):
    # get price
    url = data['AmazonURL']
    page = requests.get(url, headers={"Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"})
    soup = bs(page.text, "html.parser")
    p0 = soup.findAll("span", attrs={"class": "a-price aok-align-center reinventPricePriceToPayMargin priceToPay"})[0]
    p1 = p0.findAll("span", attrs={"class": "a-offscreen"})[0]
    print(p1.text)

    price = float(p1.text.replace('$','').replace(',',''))
    print('the price is {}'.format(price))

    #stop the code if the price greater than less_than_price
    if price > data['less_than_price']:
        return 

    # https://www.youtube.com/watch?v=g_j6ILT-X0k
    em = EmailMessage()
    em['From'] = data['email']
    em['To'] = 'JGarza9788@gmail.com'
    em['Subject'] = 'Price Alert'
    body = 'the price is below {less_than_price} \n {url}'.format(
            less_than_price=data['less_than_price'],
            url=data['AmazonURL'])
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(data['email'],data['password'])
        smtp.sendmail(
            em['From'], em['To'], em.as_string()
            )

    

    # """
    # if error sending email:
    #     https://www.google.com/settings/security/lesssecureapps
    # use TWILIO or automate it with Selenium
    # """
    # import yagmail 
    # # if price <= data['less_than_price']:
    #     # yagmail.register(data['email'], data['password'])
    #     # yag = yagmail.SMTP(data['email'])
    #     # contents = 'the price is below {less_than_price} \n {url}'.format(
    #     #     less_than_price=data['less_than_price'],
    #     #     url=data['AmazonURL'])
    #     # yag.send(data['email'], subject = "price alert", contents = contents)





if __name__ == '__main__':
    import Config
    config = Config.Config()
    # print(config.data)
    
    main(config.data)