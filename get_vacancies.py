import pandas as pd
import requests

# Токен доступа
token = 'YOUR_ACCESS_TOKEN'

# Параметры запроса
params = {
    'text': 'Аналитик',  # Желаемая позиция
    'area': 1217,  # Код региона (например, Барнаул)
    'per_page': 100  # Количество результатов на странице
}

# Отправляем GET-запрос
response = requests.get('https://api.hh.ru/vacancies', params=params, ) # headers={'Authorization': 'Bearer ' + token}

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
    item_copy = item.copy()
    item_copy['area'] = area_name
    item_copy['salary'] = salary_from
    data_new.append(item_copy)

# vacancies_df = pd.DataFrame(data['items'], columns=['id', 'name', 'area'])
vacancies_df = pd.DataFrame(data_new)


# Сохраняем DataFrame в файл
vacancies_df.to_csv('vacancies_df.csv', index=False)

# Выводим первые 5 строк DataFrame для проверки
print(vacancies_df.head())
