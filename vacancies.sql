--Создеём запрос при помощи sqlite_master

SELECT sql FROM sqlite_master WHERE type='table' AND name='new_vacancies';

PRAGMA table_info(new_vacancies);
