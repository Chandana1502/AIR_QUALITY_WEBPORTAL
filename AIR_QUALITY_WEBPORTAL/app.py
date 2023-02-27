from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OPENAQ_API_URL = "https://api.openaq.org/v1"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search():
    city = request.form['city']
    url = f"{OPENAQ_API_URL}/latest?city={city}&parameter=pm25"
    response = requests.get(url)
    data = response.json()
    if 'results' in data and len(data['results']) > 0:
        results = data['results'][0]['measurements']
        return render_template('results.html', results=results, city=city)
    else:
        return render_template('noresults.html', city=city)

if __name__ == '__main__':
    app.run()
