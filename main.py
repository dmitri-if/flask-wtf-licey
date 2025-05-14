from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def index():
    return render_template('index.html', title='Заголовок', text1='Миссия Колонизация Марса', text2='И на Марсе будут яблони цвести!')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')