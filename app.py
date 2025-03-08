from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '68aacfabf5696587d7de27738b0418e4'  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric" 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)
        if weather_data:
            return render_template('index.html', weather=weather_data)
        else:
            return render_template('index.html', error="City not found.")
    return render_template('index.html')

def get_weather_data(city):
    url = BASE_URL.format(city=city, API_KEY=API_KEY)  
    response = requests.get(url)
    data = response.json()

    if data.get('cod') == 200:  
        weather_info = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return weather_info
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)