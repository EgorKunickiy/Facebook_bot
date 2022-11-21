import pickle
import requests
from chrome import initialization_driver
from time import sleep
from facebook import fill_acc


def main(driver, cookie):
    driver.get('https://www.facebook.com/')
    sleep(5)
    for c in cookie:
        driver.add_cookie(c)

    driver.refresh()

    fill_acc(driver)

    sleep(60)


if __name__ == '__main__':
    if requests.get('http://46.227.109.143:8004/connect12').status_code == 200:
        sleep(3)
        driver = initialization_driver()
        driver.maximize_window()
        main(driver, [{'domain': '.facebook.com', 'expiry': 1669581224, 'httpOnly': False, 'name': 'wd', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': '1536x708'}, {'domain': '.facebook.com', 'expiry': 1700512336, 'httpOnly': True, 'name': 'xs', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '21%3AAMd8wIOk5C6K7A%3A2%3A1668976344%3A-1%3A-1'}, {'domain': '.facebook.com', 'expiry': 1700512336, 'httpOnly': False, 'name': 'c_user', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '100088149036134'}, {'domain': '.facebook.com', 'expiry': 1669581145, 'httpOnly': False, 'name': 'locale', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'ru_RU'}, {'domain': '.facebook.com', 'expiry': 1703536345, 'httpOnly': True, 'name': 'sb', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '0Y56Y9Cxu0Ca-Mp4NIuksenC'}, {'domain': '.facebook.com', 'expiry': 1669581224, 'httpOnly': False, 'name': 'dpr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1.25'}, {'domain': '.facebook.com', 'expiry': 1703536328, 'httpOnly': True, 'name': 'datr', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'v456Y8XHH1yqJJufAECXhi1x'}]
    )