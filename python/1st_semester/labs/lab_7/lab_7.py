from tkinter import *
from tkinter.messagebox import showinfo, showerror
from tkinter import simpledialog
from tkinter import messagebox as mb
import csv
from collections import defaultdict



def buttons():
    global button_edit, button_confirm

    button_exit = Button(root, bg = "red", command = root.destroy, text = "Выход", height = 1, width = 10)
    button_exit.pack(side=BOTTOM, fill=X)

    # button_list = Button(root, text = "Список", command = list_, bg = "#578067", height = 1, width = 10)
    # button_list.pack(side=BOTTOM, fill=X)
    #(!)
    button_seacrh = Button(root, bg = "#555555", command = new, text ="Поиск/Добавить" , height =1, width = 15)
    button_seacrh.pack(side=BOTTOM, fill=X)

    button_confirm = Button(new_window, bg = "#555555", command = search, text = "Искать",height = 1, width = 10)
    button_confirm.place(x=0,y=70)

    button_edit = Button(new_window, bg = "#676f77", command = show_edit, text = "Добавить", height = 1, width = 10)
    button_edit.place(x=190, y=70)

    button_confirm_edit = Button(new_window2,bg='#77b472', command = edit, text = "Изменить", height = 1, width = 10)
    button_confirm_edit.place(x=0, y = 165)

    # button_sort = button(window_list, bg = "#2d67c3", command = sort, text = "сортировка")
    #(!)
    button_back(window=new_window, x=110, y=100)
    button_back(window=new_window2, x=190, y=165)
    # button_back(window=window_list,x=165, y=270)
    #(!)
def button_back(window, x,y):
    b1 = Button(window, bg = "red", command = window.withdraw, text= "[назад]" )
    b1.place(x=x, y=y)

# def list_():
#     window_list.deiconify()
#     window_list.focus_set()
#     (!)



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
def edit():
    with open (r'/home/alan/Files/YandexDisk/programming/programs/labs/lab_7/lab_7.csv',"a",encoding="utf-8") as edit_text:
            edit_text.write((entry_1.get(1.0,END)).replace('\n','') + ", "+(entry_2.get(1.0,END)).replace('\n','') + ", "+ (entry_3.get(1.0,END)).replace('\n','') + ", "+(entry_4.get(1.0,END)).replace('\n','') + ", "+ (entry_5.get(1.0,END)))

def show_edit():
    new_window2.deiconify()
    new_window2.focus_set()

name = []
with open(r'/home/alan/Files/YandexDisk/programming/programs/labs/lab_7/lab_7.csv', encoding="utf-8") as name_append:
    data = csv.reader(name_append,delimiter=',')
    for i in data:
        name.append(i)
with open(r'/home/alan/Files/YandexDisk/programming/programs/labs/lab_7/lab_7.csv', encoding="utf-8") as csvfile:
    columns = defaultdict(list)
    reader = csv.DictReader(csvfile)
    for row in reader:
        for (k,v) in row.items(): columns[k].append(v)

print(name)
root = Tk()
# root.geometry(newGeometry="125x95")
root.geometry(newGeometry="125x65")
new_window = Toplevel(root)
new_window.geometry("300x130")
new_window.withdraw()
root.title("7.7")

new_window2 = Toplevel(new_window)
new_window2.geometry("270x200")
new_window2.withdraw()

# window_list = Toplevel(root)
# window_list.geometry("400x300")
# window_list.withdraw()
#(!)
Label(new_window2, text="Название").place(x=0, y=0)
Label(new_window2, text="Магазин").place(x=0, y=30)
Label(new_window2, text="Цена").place(x=0,y=60)
Label(new_window2, text="Количество").place(x=0, y=90)
Label(new_window2, text="Вес").place(x=0, y=120)
entry_1 = Text(new_window2, width = 15, height = 1)
entry_2 = Text(new_window2, width = 15, height = 1)
entry_3 = Text(new_window2, width = 15, height = 1)
entry_4 = Text(new_window2, width = 15, height = 1)
entry_5 = Text(new_window2, width = 15, height = 1)
entry_1.place(x=90, y=0)
entry_2.place(x=90, y=30)
entry_3.place(x=90, y=60)
entry_4.place(x=90, y=90)
entry_5.place(x=90, y=120)


frame = Frame(new_window)
e1 = Text(new_window, width=25, height=1)
e1.pack()
label2 = Label(new_window, text = "{0}|{1}|{2}|{3}|{4}".format(name[0][0],name[0][1],name[0][2],name[0][3],name[0][4]))
label2.pack()
label = Label(new_window)
label.pack()

buttons()
mainloop()
