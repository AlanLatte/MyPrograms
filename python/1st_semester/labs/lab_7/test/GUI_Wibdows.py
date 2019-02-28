from tkinter import *
from tkinter.messagebox import showinfo, showerror
from tkinter import simpledialog
from tkinter import messagebox as mb
import csv
from collections import defaultdict



def buttons():
    button_exit = Button(root, bg = "red", command = root.destroy, text = "Выход", height = 1, width = 10)
    button_exit.pack(side=BOTTOM)

    button_seacrh = Button(root, bg = "#555555", command = new, text ="поиск" , height =1, width = 10)
    button_seacrh.pack()

    button_confirm = Button(new_window, bg = "#555555", command = search, text = "Искать",height = 1, width = 10)
    button_confirm.pack()

def button_back(window):
    b1 = Button(window, bg = "red", command = window.withdraw, text= "назад" )
    b1.pack()

def new():
    new_window.deiconify()
    new_window.focus_set()
def search():
    s = e1.get(1.0,END)
    if s.replace("\n","") in columns['название']:
        counter = 0
        void = None
        for i in columns["название"]:
            counter+=1
            if i == s.replace("\n",""): void = name[counter]
        label['text'] = void

    else:
        label['text'] = 'Продукт не найден, добавте его'



name = []
with open(r'C:\Users\amall\YandexDisk\programming\Programs\labs\lab_7\lab_7.csv', encoding="utf-8") as name_append:
    data = csv.reader(name_append,delimiter=',')
    for i in data:
        name.append(i)
with open(r'C:\Users\amall\YandexDisk\programming\Programs\labs\lab_7\lab_7.csv', encoding="utf-8") as csvfile:
    columns = defaultdict(list)
    reader = csv.DictReader(csvfile)
    for row in reader:
        for (k,v) in row.items(): columns[k].append(v)

root = Tk()
root.geometry(newGeometry="300x350")
new_window = Toplevel(root)
new_window.geometry("300x130")
new_window.withdraw()
root.title("7.7")

new_window2 = Toplevel(new_window)
new_window2.geometry("400x300")
new_window2.withdraw()
butt_b = Button(new_window, bg = "red", command = new_window.withdraw, text= "назад" )
butt_b.pack(side=BOTTOM)
frame = Frame(new_window)
e1 = Text(new_window, width=25, height=1)
e1.pack()
label2 = Label(new_window, text = "{0}|{1}|{2}|{3}|{4}".format(name[0][0],name[0][1],name[0][2],name[0][3],name[0][4]))
label2.pack()
label = Label(new_window)
label.pack()





buttons()
mainloop()
