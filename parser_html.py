import re


def get_cod():
    pattern = 'FB-[0-9]{5}'
    with open('t.html', 'r', encoding='UTF-8') as f:
        text = f.readlines()
        result = re.search(pattern, str(text)).group()

    result = result.split('-')[1]
    return result


if __name__ == '__main__':
    print(get_cod())
