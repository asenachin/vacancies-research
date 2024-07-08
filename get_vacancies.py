import pandas as pd
import requests
from sqlalchemy import create_engine


# Токен доступа
# token = 'YOUR_ACCESS_TOKEN'

# Параметры запроса
params = {
    'text': 'Аналитик данных',  # Желаемая позиция
    'area': 1217,  # Код региона (например, Барнаул)
    'per_page': 100  # Количество результатов на странице
}

# Отправляем GET-запрос
response = requests.get('https://api.hh.ru/vacancies', params=params) # ,headers={'Authorization': 'Bearer ' + token}

# Проверка успешности запроса
if response.status_code == 200:
    # Сохранение ответа в файл
    with open('response.json', 'w') as file:
        file.write(response.text)
else:
    print(f"Ошибка запроса: {response.status_code}")

# Преобразуем JSON-ответ в DataFrame
data = response.json()


# Преобразование данных для датафрейма
data_new = []
for item in data['items']:
    area_name = item['area']['name']
    salary_from = item['salary']['from'] if item['salary'] is not None and 'from' in item['salary'] else None
    employer_name = item['employer']['name']
    snippet_requirement = item['snippet']['requirement']
    snippet_responsibility = item['snippet']['responsibility']    
    professional_roles_name = item['professional_roles'][0]['name']
    experience_name = item['experience']['name']
    employment_name = item['employment']['name']
    item_copy = item.copy()
    item_copy['area'] = area_name
    item_copy['salary'] = salary_from
    item_copy['employer'] = employer_name
    item_copy['requirement'] = snippet_requirement
    item_copy['responsibility'] = snippet_responsibility
    item_copy['professional_roles'] = professional_roles_name
    item_copy['experience'] = experience_name
    item_copy['employment'] = employment_name
    data_new.append(item_copy)

vacancies_df = pd.DataFrame(data_new, columns=['id', 
   'name', 'area', 'salary', 'created_at', 'alternate_url', 'employer', 'requirement', 
   'professional_roles', 'experience', 'employment', 'responsibility'])

# Изменим порядок столбцов
vacancies_df = vacancies_df[['id', 
   'name', 'area', 'salary', 'created_at', 'alternate_url', 'employer',  
   'professional_roles', 'experience', 'employment', 'requirement', 'responsibility']]
   
# Изменим тип данных столбца id
vacancies_df['id'] = vacancies_df['id'].astype(int)

# Преобразование столбца 'timestamp' в тип данных datetime
vacancies_df['created_at'] = pd.to_datetime(
    vacancies_df['created_at'],  format='%Y-%m-%dT%H:%M:%S%z' # format='ISO8601'
)


# Сохраняем DataFrame в файл
vacancies_df.to_csv('vacancies_df.csv', index=False)

# Выводим первые 5 строк DataFrame для проверки
print(vacancies_df.head())

# Подключимся к базе данных SQLite
engine = create_engine('sqlite:///vacancies.db')

# Запишем датафрейм в базу данных
# dtype = {'created_at': 'datetime'}
vacancies_df.to_sql('new_vacancies', engine, index=False, if_exists='replace') # , dtype=dtype

# Закрываем соединение
engine.dispose()

