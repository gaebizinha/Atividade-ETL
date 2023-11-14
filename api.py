# pip install Flask
# pip install flask_sqlalchemy
# pip install datetime
# pip install pytz

from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import requests
import pytz
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

brasil_timezone = pytz.timezone('America/Sao_Paulo')

def get_brasil_datetime():
   return datetime.now(brasil_timezone)

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_ingestao = db.Column(db.DateTime, default=get_brasil_datetime)
    data_tipo = db.Column(db.String(50))
    valores = db.Column(db.String(100))
    uso = db.Column(db.String(100))

def funcao_etl():
   
   api_key = 'd13a18996616513b72952410f7ecd170'
   cidades = ['São Paulo', 'Brasília', 'Alagoas', 'Sergipe']
   
   lista_dados_climaticos = [] 
   

   for city in cidades:
       url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
       try:
        response = requests.get(url)
        response.raise_for_status() # Raises a HTTPError if the status is 4xx, 5xx
       except requests.exceptions.RequestException as err:
        logging.error(f"Request error: {err}")
        continue

       logging.debug(f'Response status code: {response.status_code}')
       logging.debug(f'Response content: {response.json()}')
       if response.status_code == 200:
           weather_data = response.json()
           
           weather_data_json = json.dumps(weather_data)
           
           weather_entry = WeatherData(
               data_tipo='openweather',
               valores=weather_data_json,
               uso='previsao_climatica'
           )

           lista_dados_climaticos.append(weather_entry) 
           
       else:
           return f'Erro na extração dos dados da API OpenWeather para {city}', 500

   db.session.add_all(lista_dados_climaticos)
   db.session.commit()

   return lista_dados_climaticos

@app.route('/weather_data', methods=['GET'])
def display_weather_data():
  weather_data = WeatherData.query.all()
  etl_data = funcao_etl()
  return render_template('weather_table.html', weather_data=weather_data, etl_data=etl_data)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)