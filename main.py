from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/')
def index():
    return render_template('index.html', title='Заголовок', text1='Миссия Колонизация Марса', text2='И на Марсе будут яблони цвести!')

@app.route('/answer')
def answer():
    return render_template('answer.html', title='Watny', surname='Нелюбин', name='Дима', education='Ясли', profession='Отаку', sex='Мужской',
                           motivation='Люблю аниме', ready='True')

@app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', title='Почти регистрация')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')