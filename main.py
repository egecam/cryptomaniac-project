import cryptocompare
from api import API_KEY
from datetime import datetime
from graph import drawGraph

# kendi cryptocompare api'imi bagliyorum
cryptocompare.cryptocompare._set_api_key_parameter(API_KEY)

# graph cizerken ihtiyacim olan guncel saat bilgisi
now = datetime.now()


# bitcoinin amerikan dolari cinsinden degerini getiren fonksiyon


def getBTC():
    BTC = cryptocompare.get_price(currency='usd', coin='btc')
    # BTC bir nested dictionary. benim usd keyinin value bilgisine ihtiyacim var
    print(BTC['BTC']['USD'])


# input ile alinan kriptoparanin, girilen birim cinsinden degerini getiren fonksiyon


def getCoin():
    COI = input(
        'Type coin abbreviation in lowercase (for exp. "btc" for Bitcoin): ')
    CUR = input(
        'Type currency abbreviation in lowercare you want to convert (for exp. "usd" for American Dollars): ')
    # COI kriptoparanin CUR cinsinden degerini get_price metoduyla cagirip bir degiskene kaydediyorum
    coi_price = cryptocompare.get_price(currency=CUR, coin=COI)
    # salt degiskeni print edince nested dictionary tipinde bir veri yazdiriyor. sadece price degerini istedigim icin
    # dictionary'nin icinden veriyi yazdiriyorum.
    print(coi_price[COI.upper()][CUR.upper()])


# input ile alinan integer miktarinda coinleri listeleyen fonksiyon.


def coinList():
    # get_coin_list ile desteklenen coinleri cekiyorum. format(True), listeyi python list tipine donusturuyor.
    coins = cryptocompare.get_coin_list(format(True))
    q = int(input(
        'Type quantity of coins you want to sort (for exp. "10" sorts 10 coins from start): '))
    print('Coin list:')
    # 'n'.join ifadesi her bir elemani "1 satir boslugu" ile ayirmayi saglar.
    # input ile alinan q sayisina kadar olan coinleri listeliyorum.
    print('\n'.join(coins[:q]))


def draw():
    coin = input('Type coin abbreviation in uppercase (for exp. "BTC" for Bitcoin): ')
    currency = input(
        'Type currency abbreviation in uppercare you want to convert (for exp. "USD" for American Dollars): ')
    drawGraph(coin, currency)


functions = input('What do you want to do? \n a. Get live price of BTC \n b. Get live price of a coin'
                  '\n c. Get coin list \n d. Show live graph of a coin \n e. Exit(type a, b, c or exit) \n : ')

if functions == 'a':
    print('\n')
    getBTC()
    print('\n')
elif functions == 'b':
    print('\n')
    getCoin()
    print('\n')
elif functions == 'c':
    print('\n')
    coinList()
    print('\n')
elif functions == 'd':
    print('\n')
    draw()
    print('\n')
elif functions == 'exit':
    exit()
