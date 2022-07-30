#Підключаємо потрібні для роботи бібліотеки(функції)
from flask import Flask
from flask_restful import Api, Resource
from requests import get

app = Flask(__name__) #Підключаємо фреймворк
api = Api() #Підключаємо Api

response = get('https://rest.coinapi.io/v1/exchangerate/BTC/USD', headers={'X-CoinAPI-Key' : '6C5AAD9B-6CFC-4DF3-B2F1-D016F594FFFD','Accept': 'application/json'}).json() #Беремо курс BTC в USD за допомогою стороннього API
res = get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json', headers = {'Accept': 'application/json'}).json() #Беремо курс UAH до USD

try:
    UAH = int(response['rate'] * res[25]['rate']) #Отримуємо курс BTC UAH(цілочисельне значення)
except:
    UAH = 'Error loading data from https://rest.coinapi.io/v1/exchangerate/BTC/USD'

class Main(Resource):
    def get(self):
        try: #Пробуємо повернути час та курс
            return f"Time: {response['time']}. 1 BTC = {UAH} UAH."
        except: #При помилці повертаємо повідомлення
            return "Invalid status value"

api.add_resource(Main, "/api/main") #Додаємо ресурси
api._init_app(app) #Ініціалізуємо додаток

if __name__ == '__main__': #Перевіряємо чи наш додаток запускається саме з цього файлу, в інших випадках буде запущений під час виклику
    app.run(debug=True, port = 3000, host = '127.0.0.1') #Для полегшення роботи включаємо виведення debug та прописуємо наш порт і локальну адресу