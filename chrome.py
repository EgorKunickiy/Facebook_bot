from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from config import PROXY, USERAGENT


def initialization_driver():

    s = Service(r'D:\Python\bot_fb\chromedriver.exe')

    options = {
        'proxy': {
            'http': PROXY,
            'https': PROXY,
            'no_proxy': 'localhost,127.0.0.1'
        }
    }
    option = webdriver.ChromeOptions()
    option.add_argument(f'user-agent={USERAGENT}')

    driver = webdriver.Chrome(service=s, seleniumwire_options=options, options=option)

    return driver


if __name__ == '__main__':
    print(initialization_driver())