import requests
import pandas as pd

# делаем запрос к API для получения списка городов и их кодов
response = requests.get('https://api.hh.ru/areas')
data = response.json()

# создаем пустой список для хранения данных о городах
cities = []

# перебираем все регионы
for region in data:
    # для каждого региона перебираем все города
    for city in region['areas']:
        city_data = {
            'City': city['name'],
            'Area ID': city['id']
        }
        cities.append(city_data)

# создаем DataFrame из списка данных о городах
cities_df = pd.DataFrame(cities)

# сохраняем DataFrame в файл
cities_df.to_csv('city_codes.csv', index=False)

# выводим первые 5 строк DataFrame для проверки
print(cities_df.head())
