from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_price_less_than_key(price, key):
    price = int(persian_to_english(price))
    if price < key:
        return True
    else:
        return False


def persian_to_english(number):
    for i in number:
        if i in ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']:
            number = number.replace(i, str('۰۱۲۳۴۵۶۷۸۹'.index(i)))
        elif i in [',']:
            number = number.replace(i, '')
    return number


url = 'https://www.digikala.com/product/dkp-722339/%DA%A9%D8%AA%D8%A7%D8%A8-%D9%85%D8%BA%D8%A7%D8%B2%D9%87-%D8%AE%D9%88%D8%AF%DA%A9%D8%B4%DB%8C-%D8%A7%D8%AB%D8%B1-%DA%98%D8%A7%D9%86-%D8%AA%D9%88%D9%84%DB%8C/'
XPATH = '/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[3]/div[1]/div[7]/div/div[2]/div[1]/div[2]/div[2]/span'
DRIVER_PATH = 'chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
sleep_time_seconds = 7

email_message = MIMEMultipart()
email_message['from'] = 'Digikala BOT'
email_message['to'] = 'mamf20021381@gmail.com'
email_message['subject'] = 'تغییر قیمت دیجی کالا'
email_message.attach(MIMEText(f"بدو بدو قیمتش اومده پایین😍😍😍😍\n + {url}"))

while True:
    print("Started")
    driver.get(url)
    price_persian_value = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, XPATH))).text

    if is_price_less_than_key(persian_to_english(price_persian_value), 40000):
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('mamf.you@gmail.com', 'nfrqxyekxcgeniko')
            smtp.send_message(email_message)
            print('email sent')

    sleep(sleep_time_seconds)
