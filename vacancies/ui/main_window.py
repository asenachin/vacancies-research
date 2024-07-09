import tkinter as tk

from vacancies.data.vacancies_data import VacanciesDataHandler
from vacancies.db.sqlite_connection import ConnectionHandler


class MainWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1600x900")
        self.window.title("VACANCIES-RESEARCH")

        # Добавление кнопки Тест
        btn_test = tk.Button(self.window, text='Тест',
                             font=('Coureirer', 10, 'bold'), bg='#ccffcc', command=MainWindow.do_test)
        btn_test.place(x=1275, y=800, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text='Выход',
                              font=('Coureirer', 10, 'bold'), bg='#ccffcc', command=self.close)
        btn_close.place(x=1410, y=800, width=120, height=50)

    # Функция Тест
    @staticmethod
    def do_test():

        # ch = ConnectionHandler()
        # ch.do_test()

        vacancies = VacanciesDataHandler.select_list()
        for vacancy in vacancies:
            print(vacancy.name)

    # Функция закрытия главного окна программы
    def close(self):
        self.window.destroy()

    def start_mainloop(self):
        self.window.mainloop()
