import pyautogui as pg
from chrome import initialization_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import requests


def new_window(driver):
    driver.execute_script("window.open('https://google.com')")


def registration_acc(full_name: str, mail: str, password: str, driver):
    driver.get('https://www.facebook.com/')
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH, "//button[text()='Разрешить основные и необязательные cookie']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//*[text()='Создать новый аккаунт']").click()
    sleep(5)
    driver.find_element(By.NAME, 'firstname').send_keys(full_name.split()[0])
    driver.find_element(By.NAME, 'lastname').send_keys(full_name.split()[1])
    driver.find_element(By.NAME, 'reg_email__').send_keys(mail)
    driver.find_element(By.NAME, 'reg_email_confirmation__').send_keys(mail)
    driver.find_element(By.ID, 'password_step_input').send_keys(password)
    day = Select(driver.find_element(By.NAME, 'birthday_day'))
    day.select_by_visible_text('10')
    month = Select(driver.find_element(By.NAME, "birthday_month"))
    month.select_by_visible_text('июл')
    year = Select(driver.find_element(By.NAME, 'birthday_year'))
    year.select_by_visible_text('1999')
    driver.find_element(By.XPATH, "//label[text()='Женщина']").click()
    driver.find_element(By.XPATH, "//button[text()='Регистрация']").click()


def input_cod(cod: str, driver):
    driver.find_element(By.ID, 'code_in_cliff').send_keys(cod)
    sleep(1)
    driver.implicitly_wait(1)
    driver.find_element(By.NAME, 'confirm').click()
    sleep(12)
    driver.implicitly_wait(1)
    pg.moveTo(1267, 516)
    pg.click()
    sleep(13)
    pg.moveTo(1100, 939)
    pg.click()
    sleep(7)


def fill_acc(driver):
    #driver.find_element(By.XPATH, '//*[@id="mount_0_0_0H"]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span/span').click()
    pg.moveTo(41, 248)
    pg.click()
    sleep(3)
    pg.moveTo(460, 477)
    pg.click()
    sleep(3)
    return driver.current_url


if __name__ == '__main__':
    if requests.get('http://46.227.109.143:8004/connect12').status_code == 200:
        sleep(2)
        driver = initialization_driver()
        driver.maximize_window()
        second_window = 'window.open("https://www.facebook.com/", "tab2")'
        driver.execute_script(second_window)
        driver.switch_to.window('tab2')
        sleep(4)
        registration_acc('Лида Пасюк', 'xcvbhj.hgfds@interia.pl', 'Lidka693S', driver)
