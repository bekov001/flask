from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index/<name>")
def main(name):
    return render_template('base.html', name=name)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')