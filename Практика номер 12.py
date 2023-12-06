import requests
import json
from tkinter import Tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button

root = Tk()
root.title('Иванчихин Илья УБ-31')
root.geometry('400x400')

def Give_to_file():
    usname = Entry_user.get() # Получаем имя пользователя и делаем запрос
    url = f'https://api.github.com/users/{usname}'

    user_data = requests.get(url).json() # Получаем данные в json
    need_keys = ['company', 'created_at', 'email', 'id', 'name', 'url'] # Нужные ключи
    
    data = dict()
    
    for i in need_keys: # Проходим по нужным ключам и ищем подходящие пары под ключи
        data[i] = user_data.get(i) # Получаем данные по ключам и записываем в словарь
        with open('C://Users/User/Desktop/vvod.txt', 'w') as file:
            file.write(json.dumps(data, indent = 4)) # Записываем все в файл с помощью dumps. indent - количество отступов
        
lbl = Label(text='Введите Имя Пользователя: ')
lbl.grid(column=0, row=0)
Entry_user = Entry(root)
Entry_user.grid(column=0, row=1)
Button_file = Button(root, text='Получить данные', command=Give_to_file)
Button_file.grid(column=1, row=1)



root.mainloop()
