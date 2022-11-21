from chrome import initialization_driver
from konto import create_mail
from facebook import registration_acc, new_window, input_cod, fill_acc
import requests
from time import sleep
from pars_1 import create_full_name, result_csv
from parser_html import get_cod


def main():
    driver = initialization_driver()
    driver.maximize_window()
    new_window(driver)
    first_window = driver.window_handles[0]
    second_window = driver.window_handles[1]

    try:
        driver.switch_to.window(first_window)
        sleep(2)
        data = create_mail(driver)
        sleep(15)

        driver.switch_to.window(second_window)
        sleep(1)
        full_name = create_full_name()
        registration_acc(full_name, data['mail'], data['password'], driver)
        sleep(22)
        if 'confirmemail' in driver.current_url:
            driver.switch_to.window(first_window)
            sleep(10)
            driver.implicitly_wait(1)

            with open('t.html', 'w', encoding='UTF-8') as f:
                f.write(driver.page_source)

            driver.switch_to.window(second_window)
            cod = get_cod()
            #sleep(60)
            input_cod(cod, driver)
            sleep(20)
            cookie = driver.get_cookies()

            url = fill_acc(driver)

            result_csv(data, url, full_name, cookie)

            sleep(120)

        else:
            pass

    except Exception as ex:
        print(ex)
    finally:
        driver.quit()


if __name__ == '__main__':
    for i in range(5):
        if requests.get('http://46.227.109.143:8004/connect12').status_code == 200:
            sleep(3)
            main()
