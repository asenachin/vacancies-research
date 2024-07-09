import tkinter as tk
from tkinter import messagebox as mb
from vacancies.db.sqlite_connection import my_connection_handler
from vacancies.ui.main_window import MainWindow


def main():

    chk = my_connection_handler.check_connection()
    if not chk:
        root = tk.Tk()
        root.withdraw()  # Скрываем главное окно без закрытия приложения
        mb.showerror(parent=None, title="Ошибка", message="Отсутствует соединение с SQLite.")
        return

    main_window = MainWindow()
    main_window.start_mainloop()

    return 0


if __name__ == '__main__':
    main()
