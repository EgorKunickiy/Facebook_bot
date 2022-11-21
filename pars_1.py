from mimesis.providers import Person
from mimesis.enums import Gender
import csv
import random
from config import USERAGENT


person = Person("ru")


def create_password() -> str:
    password = ''.join(list(map(chr, [random.randint(97, 122) for _ in range(8)]))) + str(random.randint(100, 999)) \
               + chr(random.randint(65, 90))

    return password


def create_full_name() -> str:
    return person.first_name(gender=Gender.FEMALE) + ' ' + person.last_name(gender=Gender.FEMALE)


def write_to_csv():
    with open('names.csv', mode="w", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
        file_writer.writerow(['fullname', 'password'])
        for _ in range(100):
            full_name = create_full_name()
            file_writer.writerow([full_name, create_password()])


def result_csv(data: dict, url, full_name, cookie):
    with open('result.csv', mode="a+", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
        #file_writer.writerow(['Логин/Пароль(почта)', 'Логин/Пароль', 'Ссылка на акк', 'Имя/Фамилия', 'User Agent', 'Куки'])
        file_writer.writerow([data['mail']+':'+data['password'], data['mail']+':'+data['password'], url, full_name, USERAGENT, cookie])


if __name__ == "__main__":
    write_to_csv()
