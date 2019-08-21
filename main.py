import tkinter as tk
import request

def sel_original_currency():
    selection = var.get()
    mocu.config(text=selection)


def sel_target_currency():
    selection  = var_target.get()
    mtcu.config(text=selection)

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

button = tk.Button(frameTop, text='開始換算')
button.pack(side='right')

root.mainloop()