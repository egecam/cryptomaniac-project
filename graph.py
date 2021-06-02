# main.py'da GUI araciligiyla kullanicidan alinan kriptopara ve para birimi degerleri kullanilarak
# matplotlib kutuphanesiyle grafik cizilir

from datetime import datetime
from currency_symbols import CurrencySymbols
import cryptocompare
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from api import API_KEY

cryptocompare.cryptocompare._set_api_key_parameter(API_KEY)

#  coin ve cur parametreleriyle cagrilabilen, grafik cizen fonksiyon
# bu iki parametreyi daha sonra kullanicidan GUI uzerinden alacagim


def drawGraph(coin, cur):
    plt.style.use('dark_background')

    # once x ve y degerlerini bos birakiyorum
    x_vals = []
    y_vals = []

    # main.py'daki gibi coin price'ina erisiyorum
    def getCoinPrice(crpcoin, currency):
        return cryptocompare.get_price(crpcoin, currency=currency)[crpcoin][currency]

    # get_coin_list metodundan sadece coinin adini aliyorum
    def getCoinName(crpcoin):
        return cryptocompare.get_coin_list()[crpcoin]['FullName']

    # canli grafigi cizen asil fonksiyon
    def animate(i):
        # grafik anlik olarak cizilecegi icin append metodunu kullaniyorum
        # x degerlerine her saniye guncel saat bilgisi eklenecek
        # y degerlerine her saniye guncel coin price degeri eklenecek
        x_vals.append(datetime.now())
        y_vals.append(getCoinPrice(coin, cur))

        plt.cla()
        plt.title(getCoinName(coin) + ' Live Graph')

        plt.xlabel('Date')
        plt.ylabel(f'Price ({CurrencySymbols.get_symbol(cur)})')
        plt.plot_date(x_vals, y_vals, linestyle="solid", ms=0)
        plt.tight_layout()
    # aldigimiz bilgilerle figur cizen metodu, 'ani' degiskenine gonderiyorum
    # interval=1000 bunun her 1000 milisaniye yani 1 saniyede yapilacagini belirtiyor
    # animate, grafigin statik degil dinamik olacagini belirtiyor
    ani = FuncAnimation(plt.gcf(), animate, interval=1000)

    plt.show()
