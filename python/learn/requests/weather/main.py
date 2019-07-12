import requests


def main(url):
    print(requests.get(url).text)

if __name__ == '__main__':
    main_url = "http://wttr.in/"
    city =  "Moscow"    \
    + "?"
    format = "format="  \
    + "%l:+%c%t +%w&period=60"
    main(url = main_url + city + format)
