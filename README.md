# Автотесты UI и API для веб-приложения "Кинопоиск"
## Описание задачи
Этот проект содержит набор автоматизированных тестов для API и UI с использованием инструментов (pytest, requests, selenium, allure) веб-приложения Кинопоиск. 

## Цель проекта
Главная цель проекта — гарантировать высокое качество и стабильность работы Kinopoisk через автоматизацию тестирования. Это позволяет обнаруживать и устранять потенциальные ошибки на ранних этапах разработки, повышая надежность и улучшая пользовательский опыт сервиса.

## Структура проекта
config.py: Конфигурационный файл.
search_page.py: Файл для взаимодействия с элементами страницы поиска.
test_api.py: Автотесты API.
test_ui.py: Автотесты UI.
requirements.txt: Список установленных зависимостей.

## Установка зависимостей
Перед работой с проектом установить все зависимости:
pip install -r requirements.txt

## Запуск тестов
### API Тесты
Запуск тестов API:
pytest -v --alluredir=allure-results test_api.py

### UI Тесты
Запуск тестов UI:
pytest -v --alluredir=allure-results test_ui.py

### Просмотр отчетов Allure
Чтобы сгенерировать и просмотреть отчеты Allure после выполнения тестов, выполните следующие шаги:

1. Генерация отчета:
   allure serve allure-results
2. После выполнения команды откроется браузер с подробным отчетом.

## Финальный проект

- [Ссылка на финальный проект по ручному тестированию](https://boundless-cafe-e4f.notion.site/c78fbad9876d42beb1cfc802eaf92602?pvs=4)


