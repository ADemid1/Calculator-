import tkinter as tk

def add(b):
    v = a.get()
    if v[0] == "0":
        v = v[1:]
    a.delete(0, tk.END)
    a.insert(0, v + b)

def add_o(o):
    v = a.get()
    if v[-1] in '-+*/':
        v = v[:-1]
    a.delete(0, tk.END)
    a.insert(0, v + o)

def add_calc():
    v = a.get()
    if v[-1] in '-+*/':
        v = v + v[:-1]
    a.delete(0, tk.END)
    a.insert(0, eval(v))

def add_ce():
    a.delete(0, tk.END)
    a.insert(0, '0')

def make_Button(n):
    return tk.Button(text=n, bd=5, font=('Arial', 13), command=lambda: add(n))

def make_Button_o(o):
    return tk.Button(text=o, bd=5, font=('Arial', 13), fg="red", command=lambda: add_o(o))

def make_Button_calc(o):
    return tk.Button(text=o, bd=5, font=('Arial', 13), fg="red", command=lambda: add_calc())

def make_Button_ce():
    return tk.Button(text="ce", bd=5, font=('Arial', 13), fg="red", command=lambda: add_ce())

#Создаем графический интерфейс
w = tk.Tk()
w.geometry('240x260+100+200')#Размер для окна
w.title("Kalkulate")
w["bg"] = "#00FF00"

a = tk.Entry(w, justify=tk.RIGHT, font=("Arial", 15), width=15)
a.insert(0, "0")
a.grid(row=0, column=0, columnspan=4, stick="we", padx=5)

make_Button("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_Button("2").grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_Button("3").grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_Button("4").grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_Button("5").grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_Button("6").grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_Button("7").grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_Button("8").grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_Button("9").grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_Button("0").grid(row=4, column=1, stick="wens", padx=5, pady=5)

make_Button_o("+").grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_Button_o("-").grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_Button_o("*").grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_Button_o("/").grid(row=4, column=3, stick="wens", padx=5, pady=5)

make_Button_calc("=").grid(row=4, column=2, stick="wens", padx=5, pady=5)

make_Button_ce().grid(row=4, column=0, stick="wens", padx=5, pady=5)

w.grid_columnconfigure(0, minsize=60)
w.grid_columnconfigure(1, minsize=60)
w.grid_columnconfigure(2, minsize=60)
w.grid_columnconfigure(3, minsize=60)
#row - строка
#column - столбец
w.grid_rowconfigure(1, minsize=60)
w.grid_rowconfigure(2, minsize=60)
w.grid_rowconfigure(3, minsize=60)
w.grid_rowconfigure(4, minsize=60)

w.mainloop()#Вывод на экран