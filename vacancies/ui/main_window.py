import tkinter as tk


class MainWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("640x480")
        self.window.title("VACANCIES-RESEARCH")

        # Добавление кнопки Тест
        btn_test = tk.Button(self.window, text='Тест',
                              font=('Coureirer', 10, 'bold'), bg='#ccffcc', command=self.do_test)
        btn_test.place(x=25, y=300, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text='Выход',
                              font=('Coureirer', 10, 'bold'), bg='#ccffcc', command=self.close)
        btn_close.place(x=160, y=300, width=120, height=50)


    # Функция Тест
    def do_test(self):
        pass

    # Функция закрытия главного окна программы
    def close(self):
        self.window.destroy()

    def start_mainloop(self):
        self.window.mainloop()