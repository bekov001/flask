from random import choice

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index/<name>")
def main(name):
    return render_template('base.html', name=name)


@app.route("/training/<prof>")
def train(prof):
    return render_template("index.html", text=choice(("Научные симуляторы", "Инженерные тренажеры")), prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')