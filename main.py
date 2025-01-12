from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import requests # запрос на сайт
import pyperclip


def upload():
    try:
        filepath = fd.askopenfilename()
        if filepath:
            with open(filepath, 'rb') as f:
                files = {'file': f}
                response = requests.post('https://file.io', files=files)
                response.raise_for_status()
                link = response.json()['link']
                entry.delete(0, END)
                entry.insert(0, link)
                pyperclip.copy(link) # отправили в буфер обмена
                mb.showinfo("Ссылка скопирована", f"Ссылка '{link}' успешно скопирована в буфер обмена")
                print(response)
    except Exception as e:
        mb.showerror("Ошибка", f"Произошла ошибка: {e}")

window = Tk()
window.title("Сохранение файлов в облаке")
window.geometry("400x200")

button = ttk.Button(text="Загрузить файл", command=upload) #upload-загрузка
button.pack()

# поле ввода на который будет выведена ссылка
entry = ttk.Entry()
entry.pack()

window.mainloop()
