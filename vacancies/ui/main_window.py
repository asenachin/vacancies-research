import tkinter as tk
from tkinter import ttk

from vacancies.data.vacancies_data import VacancyDataObject, VacancyDataHandler


class MainWindow:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1600x900")
        self.window.title("Персональный трекер поиска работы")

        # Создаем вкладки
        self.tab_control = ttk.Notebook(self.window)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)

        # Добавляем вкладки
        self.tab_control.add(self.tab1, text="Вакансии")
        self.tab_control.add(self.tab2, text="Отклики")

        # Добавление кнопки Тест
        btn_test = tk.Button(self.tab1, text='Тест',
                             font=('Arial', 10, 'bold'), bg='#ccffcc', command=self.do_test)
        btn_test.place(x=1190, y=800, width=120, height=50)

        # Добавление кнопки Вакансии
        btn_test = tk.Button(self.tab1, text='Вакансии',
                             font=('Arial', 10, 'bold'), bg='#ccffcc', command=self.do_list_vacancies)
        btn_test.place(x=1320, y=800, width=120, height=50)

        # Добавление кнопки закрытия программы
        btn_close = tk.Button(self.window, text='Выход',
                              font=('Arial', 10, 'bold'), bg='#ccffcc', command=self.close)
        btn_close.place(x=1450, y=824, width=120, height=50)

        # Создаем виджет Treeview
        self.tree = ttk.Treeview(self.tab1, columns=('Column1', 'Column2', 'Column3', 'Column4', 'Column5',
                                                     'Column6', 'Column7', 'Column8', 'Column9', 'Column10',
                                                     'Column11', 'Column12'),
                                 show='headings', height=800)

        self.tree.heading('Column1', text='id')
        self.tree.heading('Column2', text='name')
        self.tree.heading('Column3', text='area')
        self.tree.heading('Column4', text='salary')
        self.tree.heading('Column5', text='created_at')
        self.tree.heading('Column6', text='alternate_url')
        self.tree.heading('Column7', text='employer')
        self.tree.heading('Column8', text='professional_roles')
        self.tree.heading('Column9', text='experience')
        self.tree.heading('Column10', text='employment')
        self.tree.heading('Column11', text='requirement')
        self.tree.heading('Column12', text='responsibility')
        self.tree.place(x=25, y=25, width=1550, height=750)

        # Создание вертикальной поломы прокрутки
        vsb = ttk.Scrollbar(self.tab1, orient="vertical", command=self.tree.yview)
        vsb.place(x=1575, y=25, height=750)
        self.tree.configure(yscrollcommand=vsb.set)

        # Создание горизонтальной полосы прокрутки
        hsb = ttk.Scrollbar(self.tab1, orient="horizontal", command=self.tree.xview)
        hsb.place(x=25, y=775, width=1550)
        self.tree.configure(xscrollcommand=hsb.set)

        # Упаковываем вкладки
        self.tab_control.pack(expand=1, fill="both")

    def do_test(self):

        # ch = ConnectionHandler()
        # ch.do_test()

        # vacancies = VacanciesDataHandler.select_list()
        # for vacancy in vacancies:
        #     print(vacancy.name)

        # self.get_report_text()

        # VacanciesDataHandler.delete_by_id(97034185)
        # print('Готово!')

        # vacancy_update = VacancyDataHandler.select_by_id(91350026)
        # print(vacancy_update.vacancy_id, vacancy_update.name)
        # vacancy_update.name = 'Консультант/аналитик 1С ERP (управление производственными процессами)'
        # print(vacancy_update.vacancy_id, vacancy_update.name)
        # VacancyDataHandler.update(vacancy_update)
        # print('Готово!')

        vacancy_insert = VacancyDataObject(name="Консультант/аналитик 1С ERP")
        print(vacancy_insert.name)
        VacancyDataHandler.insert(vacancy_insert)
        print(vacancy_insert.vacancy_id)
        print('Готово!')

    # Открытие списка "Отделы"
    def do_list_vacancies(self):
        self.get_report_text()

    def close(self):
        self.window.destroy()

    def start_mainloop(self):
        self.window.mainloop()

    def get_report_text(self):
        vacancies = VacancyDataHandler.select_list()
        for vacancy in vacancies:
            self.tree.insert("", 'end', text=vacancy.vacancy_id,
                             values=(vacancy.vacancy_id, vacancy.name, vacancy.area, vacancy.salary, vacancy.created_at,
                                     vacancy.alternate_url, vacancy.employer, vacancy.professional_roles,
                                     vacancy.experience, vacancy.employment, vacancy.requirement,
                                     vacancy.responsibility))
