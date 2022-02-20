from random import choice

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index/<name>")
def main(name):
    return render_template('base.html', name=name)


@app.route("/training/<prof>")
def train(prof):
    return render_template("index.html", text=choice(("Научные симуляторы", "Инженерные тренажеры")), prof=prof)


@app.route('/distribution')
def distribution():
    return render_template('list.html', astronauts=astronauts)


if __name__ == '__main__':
    astronauts = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни',
                  'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    app.debug = True
    app.run(port=8080, host='127.0.0.1')