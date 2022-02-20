from random import choice

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index/<name>")
def main(name):
    return render_template('base.html', name=name)


@app.route("/training/<prof>")
def train(prof):
    return render_template("index.html", text=choice(("Научные симуляторы", "Инженерные тренажеры")), prof=prof)


@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    profil = {}
    profil['title'] = 'Анкета'
    profil['surname'] = 'Watny'
    profil['name'] = 'Mark'
    profil['education'] = 'выше среднего'
    profil['profession'] = 'штурман марсохода'
    profil['sex'] = 'male'
    profil['motivation'] = 'Всегда мечтал застрять на Марсе!'
    profil['ready'] = 'True'
    return render_template('answer.html', **profil)



if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, host='127.0.0.1')