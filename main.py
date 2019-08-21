import tkinter as tk
import requests
from bs4 import BeautifulSoup

def get_url():
    url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    r = requests.get(url, headers = headers, allow_redirects=False)
    # print(r.status_code) # 200表示訪問成功
    # print(r.url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup


def get_exchange_data(soup):
    exchange_rate = {}
    # 0 = USD
    # 7 = JPY
    # 8 = ZAR
    # 14 = EUR
    USD = soup.select('tbody')[0].select('tr')[0].select('td')[4].text
    JPY = soup.select('tbody')[0].select('tr')[7].select('td')[4].text
    ZAR = soup.select('tbody')[0].select('tr')[8].select('td')[4].text
    EUR = soup.select('tbody')[0].select('tr')[14].select('td')[4].text

    print(USD, JPY, ZAR, EUR)
    


def main():

    def sel_original_currency():
        selection = var.get()
        mocu.config(text=selection)


    def sel_target_currency():
        selection  = var_target.get()
        mtcu.config(text=selection)


    def testbuttonfunc():
        label_op.config(text='i got huge dick')


    get_url()
    get_exchange_data(get_url())

    root = tk.Tk()
    root.title('Currency Exchange Rate Calculator')

    Canvas = tk.Canvas(root, height=500, width=600, bg='#91b2e3')
    Canvas.pack()

    # frame-放置要換算幣別的entry、換算完成的entry、執行按鈕、換算幣別的匯率、menu button
    frameTop = tk.Frame(root, bg='#eb8dcd', bd=5)
    frameTop.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.1)

    # 原貨幣單位menu button : menu original curreny unit
    mocu = tk.Menubutton(frameTop, text='幣別', bg='orange')
    mocu.pack(side='left')
    # 原貨幣單位menu button的內容
    var = tk.StringVar()
    mocu.menu = tk.Menu(mocu, tearoff=0)
    mocu['menu'] = mocu.menu
    mocu.menu.add_radiobutton(label='美金', variable=var, value='USD', command=sel_original_currency)
    mocu.menu.add_radiobutton(label='臺幣', variable=var, value='TWD', command=sel_original_currency)
    mocu.menu.add_radiobutton(label='歐元', variable=var, value='EUR', command=sel_original_currency)
    mocu.menu.add_radiobutton(label='日幣', variable=var, value='JPY', command=sel_original_currency)
    mocu.menu.add_radiobutton(label='南非幣', variable=var, value='ZAR', command=sel_original_currency)

    # 數量輸入框
    entryOriCurreny = tk.Entry(frameTop, bg='white', bd=1, font='courier 24')
    entryOriCurreny.place(relwidth=0.35, relheight=1, relx=0.15)

    # 敘述換成哪一國的貨幣
    label_des = tk.Label(frameTop, text='換為：', bg='#eb8dcd')
    label_des.place(relx=0.525, relheight=1)

    # 選擇要換哪一國的貨幣（menu button:menu target currency unit）
    mtcu = tk.Menubutton(frameTop, text='目標貨幣', bg='#eb8dcd')
    mtcu.place(relx=0.65, relheight=1)

    var_target = tk.StringVar()
    mtcu.menu = tk.Menu(mtcu, tearoff=0)
    mtcu['menu'] = mtcu.menu
    mtcu.menu.add_radiobutton(label='美金', variable=var_target, value='USD', command=sel_target_currency)
    mtcu.menu.add_radiobutton(label='臺幣', variable=var_target, value='TWD', command=sel_target_currency)
    mtcu.menu.add_radiobutton(label='歐元', variable=var_target, value='EUR', command=sel_target_currency)
    mtcu.menu.add_radiobutton(label='日幣', variable=var_target, value='JPY', command=sel_target_currency)
    mtcu.menu.add_radiobutton(label='南非幣', variable=var_target, value='ZAR', command=sel_target_currency)

    # 確認換算按鈕

    button = tk.Button(frameTop, text='開始換算', command=testbuttonfunc)
    button.pack(side='right')

    # 下方的frame
    frameLower = tk.Frame(root, bg='#8debe0', bd=10)
    frameLower.place(relx=0.1, rely=0.25,relwidth=0.8, relheight=0.6)

    # 輸出換算結果
    label_op = tk.Label(frameLower, bg='white', bd=5)
    label_op.place(relwidth=1, relheight=0.5)

    #輸出當前匯率
    label_rate = tk.Label(frameLower, bg='pink', bd=5)
    label_rate.place(relwidth=1, relheight=0.5,rely=0.5)

    root.mainloop()


main()





















