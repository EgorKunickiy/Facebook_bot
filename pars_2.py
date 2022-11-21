import requests


def main():
    n = int(input())
    for i in range(n):
        r = requests.get("https://thispersondoesnotexist.com/image")
        with open(f"D:\\work\\image{i+1}.jpg", "wb")as img:
            img.write(r.content)


if __name__ == "__main__":
    main()
