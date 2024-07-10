from vacancies.db.sqlite_connection import my_connection_handler


class VacanciesDataObject:
    def __init__(self, id=0, name='', area='', salary='', created_at='', alternate_url='', employer='',
                 professional_roles='', experience='', employment='', requirement='', responsibility=''):
        self.vacancy_id = id
        self.name = name
        self.area = area
        self.salary = salary
        self.created_at = created_at
        self.alternate_url = alternate_url
        self.employer = employer
        self.professional_roles = professional_roles
        self.experience = experience
        self.employment = employment
        self.requirement = requirement
        self.responsibility = responsibility


class VacanciesDataHandler:
    @staticmethod  # Принадлежит классу в целом
    def select_list():
        vacancies = []
        try:
            mydb = my_connection_handler.get_connection()
            select_query = "SELECT * FROM new_vacancies ORDER BY name"
            cursor = mydb.cursor()
            cursor.execute(select_query)
            result = cursor.fetchall()
            for row in result:
                vacancies.append(VacanciesDataObject(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                                     row[7], row[8], row[9], row[10], row[11]))
            return vacancies
        except:
            raise

    @staticmethod
    def get_vacancy(row):
        return VacanciesDataObject(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                   row[7], row[8], row[9], row[10], row[11])

    @staticmethod
    def select_by_id(vacancy_id: int):
        mydb = my_connection_handler.get_connection()
        select_query = "SELECT * FROM new_vacancies WHERE id=" + str(vacancy_id)
        cursor = mydb.cursor()
        cursor.execute(select_query)
        row = cursor.fetchone()
        department = VacanciesDataHandler.get_vacancy(row)
        return department
