from random import choice

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index/<name>")
def main(name):
    return render_template('base.html', name=name)


@app.route("/training/<prof>")
def train(prof):
    return render_template("index.html", text=choice(("Научные симуляторы", "Инженерные тренажеры")), prof=prof)


@app.route('/list_prof/<type_lst>')
def index(type_lst):
    return render_template('list.html', url=type_lst, professions=profs)


profs = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']


if __name__ == '__main__':
    app.debug = True
    app.run(port=8080, host='127.0.0.1')