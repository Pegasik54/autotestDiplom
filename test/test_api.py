import requests 
import allure
from config import URL_API, HEADERS

@allure.title("Поиск фильма и персоны")
@allure.description("Выполнение теста на поиск контента на поиск контента по ID")
@allure.id(1)
@allure.severity("Критический")
def test_search_content_by_id():
    
    with allure.step("Указываем GET запроса с ID"):
        response = requests.get(f"{URL_API}/movie/666", headers=HEADERS)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200

@allure.title("Поиск сериала по названию")
@allure.description("Выполнение теста на поиск сериала по заданному названию")
@allure.id(2)
@allure.severity("Критический")
def test_search_content_by_title():
  
    with allure.step("Указываем GET запрос с названием контента"):
        response = requests.get(f"{URL_API}/movie/search?page=1&limit=10&query=Сёгун", headers=HEADERS)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200

@allure.title("Поиск персоны")
@allure.description("Выполнение теста на поиск персоны")
@allure.id(3)
@allure.severity("Критический")
def test_search_person_by_name():
    
    with allure.step("Отправка GET запроса на"):
        response = requests.get(f"{URL_API}//person/search?page=1&limit=10&query=КиануРивз", headers=HEADERS)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200

@allure.title("Поиск персоны (Негативный)")
@allure.description("Выполнение теста на поиск персоны с ошибкой в запросе")
@allure.id(4)
@allure.severity("Критический")
def test_search_content_invalid_params():
    
    with allure.step("Отправка GET запроса с ошибкой"):
        response = requests.get(f"{URL_API}/person/search?page=1&limit=10query=КиануРивз", headers=HEADERS)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 400

@allure.title("Поиск фильма (Негативный)")
@allure.description("Выполнение теста на поиск фильма с несуществеющим ID")
@allure.id(5)
@allure.severity("Критический")
def test_search_content_id_out_of_bounds():
   
    with allure.step("Указываем GET запроса с негативным ID"):
        response = requests.get(f"{URL_API}/movie/365.65", headers=HEADERS)
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 404