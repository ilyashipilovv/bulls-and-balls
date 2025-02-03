from tkinter import *
from tkinter import ttk
from random import randint as rnd
from datetime import *
from tkinter.messagebox import showerror

root = Tk()
root.title("Bulls and Balls")
root.geometry("800x600+200+50")
root.resizable(False, False)
root.configure(bg='royalblue3')



def start_button():  # Кнопка запуска игры
    def close_window():
        global user_name
        user_name = combobox.get()
        window.destroy()
    global start_game
    global tries
    global four_num
    global end_game_label
    start_game = datetime.now()    #Фиксируем время старта игры
    bik = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    four_num = ""
    tries = 0   #Создаем основные переменные и список нужных чисел
    for _ in range(4):
        a = rnd(0, len(bik) - 1)
        four_num += str(bik[a]) #Рандомно генерируем 4 числа из списка.
        del bik[a]  #Чтобы числа не повторялись удаляем взятое из списка(можно переписать с другим методом РАНДОМА)
    listbox_ind = tries_listbox.size()
    tries_listbox.delete(0, listbox_ind)
    end_game_label = ttk.Label(text="", background='royalblue3', font=("Arial", 28))
    end_game_label.place(x=200, y=400, height=200, width=575)
    enter_field_1.delete(0, END)
    enter_field_2.delete(0, END)
    enter_field_3.delete(0, END)
    enter_field_4.delete(0, END)
    btn_vvod["state"] = "normal"
    window = Tk()
    window.title("Имя Игрока")
    window.geometry("250x150+500+200")
    with open(f'E:\\Python\\быки и коровы\\Рекорды.txt', 'r', encoding="utf-8") as input_file:
        users = list({el.split()[0] for el in input_file.readlines()}) 
    combobox = ttk.Combobox(window, values=users, font=("Arial", 12))
    combobox.place(x=20, y=20)
    close_button = ttk.Button(window, text="Подтвердить", command=close_window)
    close_button.place(x=20, y=60, height=70, width=200)
    




def vvod_button():  # Кнопка ввода
    def vvod_is_valid(vvod):
        flag = True
        if len(vvod) != 4:
            flag = False
        elif vvod.isdigit() == False:
            flag = False
        elif len({el for el in vvod}) != 4:
            flag = False
        return flag
        
    global tries
    global four_num
    global start_game
    global end_game_label
    global user_name
    cows = 0
    bulls = 0
    vvod = "".join([enter_field_1.get(), enter_field_2.get(), enter_field_3.get(), enter_field_4.get()])
    if vvod_is_valid(vvod) == False:
        showerror(title="Ошибка", message="Некорректный ввод")
        enter_field_1.delete(0, END)
        enter_field_2.delete(0, END)
        enter_field_3.delete(0, END)
        enter_field_4.delete(0, END)
    else:
        tries += 1 #Считаем попытки
        if vvod == four_num: #Если угадали
            finish_game = datetime.now()  #Фиксируем время финиша
            time_of_game = str(finish_game - start_game)[:11] #Считаем время игры
            game_date = "/".join(list(str(finish_game)[:10].split("-"))[::-1])
            end_game_label = ttk.Label(text=f"Поздравляю! Ты победил!\nВремя игры: {time_of_game}\nПопыток: {tries}", background='royalblue3', font=("Arial", 28))
            end_game_label.place(x=200, y=400, height=200, width=575)
            with open(f'E:\\Python\\быки и коровы\\Рекорды.txt', 'a', encoding="utf-8") as output_file:
                output_file.write(f"{user_name} - Время игры: {time_of_game}; Попыток: {tries}; Дата: {game_date}\n")
        
        for k in range(0, 4):
            if vvod[k] == four_num[k]: #Считаем количество совпавших чисел по позиции
                bulls += 1
            elif vvod[k] in four_num and vvod[k] != four_num[k]: #Считаем количество чисел не совпавших по позиции
                cows += 1
        listbox_ind = tries_listbox.size()
        tries_listbox.insert(listbox_ind, f" {vvod} - {bulls}Б : {cows}K")
        cows = 0
        bulls = 0
    



number_1 = ttk.Label(text=" ?", font=("Arial", 80), background='lightblue')
number_1.place(x=180, y=50, height=125, width=125)
number_2 = ttk.Label(text=" ?", font=("Arial", 80), background='lightblue')
number_2.place(x=330, y=50, height=125, width=125)
number_3 = ttk.Label(text=" ?", font=("Arial", 80), background='lightblue')
number_3.place(x=480, y=50, height=125, width=125)
number_4 = ttk.Label(text=" ?", font=("Arial", 80), background='lightblue')
number_4.place(x=630, y=50, height=125, width=125)

enter_field_1 = ttk.Entry(font=("Arial", 100), background='blue', justify=CENTER)
enter_field_1.place(x=180, y=200, height=125, width=125)
enter_field_2 = ttk.Entry(font=("Arial", 100), justify=CENTER)
enter_field_2.place(x=330, y=200, height=125, width=125)
enter_field_3 = ttk.Entry(font=("Arial", 100), justify=CENTER)
enter_field_3.place(x=480, y=200, height=125, width=125)
enter_field_4 = ttk.Entry(font=("Arial", 100), justify=CENTER)
enter_field_4.place(x=630, y=200, height=125, width=125)

tries_listbox = Listbox(font=("Arial", 16), bg="royalblue1", fg="white", listvariable=start_button)
tries_listbox.place(x=0, y=0, width=150, height=600)

scrollbar = ttk.Scrollbar(orient="vertical", command=tries_listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
  
tries_listbox["yscrollcommand"]=scrollbar.set

btn_start = ttk.Button(text="Start", command=start_button)
btn_start.place(x=480, y=350, width=270, height=50)

btn_vvod = ttk.Button(text="Enter", command=vvod_button, state=["disabled"])
btn_vvod.place(x=180, y=350, width=270, height=50)

root.mainloop()
