from flask import Flask, url_for, request, render_template
import random
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def index():
    return render_template('index.html', title='Заголовок', text1='Миссия Колонизация Марса', text2='И на Марсе будут яблони цвести!')

@app.route('/member')
def member():
    with open('templates/jsn.json', encoding='utf-8') as file:
        data = json.load(file)
        return render_template('member.html', title='Личная карточка', people=data['members'][random.randint(0, 5)])

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')