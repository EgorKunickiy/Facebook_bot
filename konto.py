import requests
from selenium.webdriver.common.by import By
import pyautogui as pg
from time import sleep
from filling import text, number, date
from chrome import initialization_driver
from pars_1 import create_password


def create_mail(driver):
    driver.get('https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe')
    driver.find_element(By.CLASS_NAME, 'rodo-popup-agree').click()
    first_name = text()
    driver.find_element(By.CLASS_NAME, '_2E5nhefoauyex').send_keys(first_name)
    pg.moveTo(1030, 435)
    pg.click()
    last_name = text()
    pg.typewrite(last_name)
    driver.find_element(By.NAME, 'birthdayDay').send_keys(number())
    driver.find_element(By.NAME, 'birthdayYear').send_keys(date())
    driver.find_element(By.XPATH, "//*[text()='Miesiąc']").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[text()='Luty']").click()
    driver.find_element(By.XPATH, "//*[text()='Płeć']").click()
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//*[text()='Kobieta']").click()
    sleep(1)
    pg.moveTo(543, 604)
    pg.click()
    sleep(1.5)
    password = create_password()
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'rePassword').send_keys(password)
    driver.find_element(By.CLASS_NAME, "checkbox-wrapper").click()
    bt = driver.find_element(By.XPATH, "//*[text()='Załóż darmowe konto']")
    driver.execute_script("arguments[0].scrollIntoView();", bt)
    sleep(2)
    bt.click()

    return {'mail': first_name + '.' + last_name + '@interia.pl', 'password': password}


if __name__ == '__main__':
    if requests.get('http://46.227.109.143:8004/connect12').status_code == 200:
        sleep(2)
        driver = initialization_driver()
        driver.maximize_window()
        first_window = 'window.open("https://konto-pocztowe.interia.pl/#/nowe-konto/darmowe", "tab1")'
        driver.execute_script(first_window)
        driver.switch_to.window('tab1')
        sleep(4)
        create_mail(driver)
        sleep(60)
