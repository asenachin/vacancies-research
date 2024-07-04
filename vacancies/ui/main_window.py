import tkinter as tk


class MainWindow:

    # Конструктор
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("640x480")
        self.window.title("VACANCIES-RESEARCH")

    # Запуск цикла окна
    def start_mainloop(self):
        self.window.mainloop()