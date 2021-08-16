from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import yagmail


session = HTMLSession()

URL = "https://www.bathandbodyworks.com/p/autumn-woods-3-wick-candle-026333411.html?cm_sp=Search-_-Results-_-026333411&trackingid=prodType"
page = session.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

manuf_elem = prod_name = soup.find("div", class_="small-title")

candle = manuf_elem.next_sibling.strip()
wicks = soup.find("span", class_="small-title").text
manufacturer = manuf_elem.text
price = soup.find("span", class_="price-sales").text
availability = soup.find("div", class_="in-stock-msg").text.strip()

if availability == 'Available':
    in_stock = 'is available'
else:
    in_stock = 'is not available'

email_message = "The {} {} by {} {} for {} here: \n{}".format(candle, wicks, manufacturer, in_stock, price, URL)

sender_email = "candlesender@gmail.com"
receiver_email = "user@gmail.com"
subject = "Candle link test"
sender_password = input(f'Please enter the password for {sender_email}:\n') 

yag = yagmail.SMTP(user=sender_email, password=sender_password)

contents = [
    "Hello,",
    email_message,
    "Regards,",
    "The candle sender"
]

yag.send(receiver_email, subject, contents)


