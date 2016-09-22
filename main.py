import requests

url = 'http://booking.uz.gov.ua/purchase/search/'
cookies = {
    '_gv_lang': 'uk',
    '_gv_sessid': 'j4hs9lfdtab2uk94uc06mp45b1',
    'HTTPSERVERID': 'server2',
}

headers = {
    'GV-Ajax': '1',
    'GV-Token': '714cc5e6ab083086fb7c451d98faf077',
    'Origin': 'http://booking.uz.gov.ua',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'uk-UA,uk;q=0.8,ru;q=0.6,en-US;q=0.4,en;q=0.2',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Referer': 'http://booking.uz.gov.ua/',
    'Connection': 'keep-alive',
    'GV-Screen': '1366x768',
    'GV-Referer': 'http://booking.uz.gov.ua/',
}

data = 'station_id_from=2208001&station_id_till=2200001&station_from=%D0%9E%D0%B4%D0%B5%D1%81%D0%B0&station_till=%D0%9A%D0%B8%D1%97%D0%B2&date_dep=12.06.2016&time_dep=15%3A00&time_dep_till=&another_ec=0&search='

import time, os

while True:
    try:
        r = requests.post(url, headers=headers, cookies=cookies, data=data)
    except Exception:
        print("Error")
    ticket = False
    for i in r.json()["value"]:
        print(i)
        try:
            for k in i["types"]:
                if k['letter'] == 'П':
                    ticket = True
        except:
            break
    if ticket:
        print('TICKET!')
        os.system('play beep39.mp3')
    else:
        print('nothing...')
        time.sleep(5)

