from datetime import date
from flask import Flask, render_template
import requests

app = Flask(__name__)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 '
                  'Safari/537.36 Edg/106.0.1370.47 '
}
url = 'https://api.ahfi.cn/api/lsjt'
params = {
    'format': 'json'
}
today = date.today()


with requests.get(url, headers=headers, params=params) as r:
    day = r.json()['day']
    text = r.json()['content']

content = text


@app.route('/')
def index():
    return render_template("index.html", content=content, today=today)


if __name__ == '__main__':
    app.run()
