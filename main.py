from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "<strong>Миссия Колонизация Марса</strong>"


@app.route('/index')
def mission():
    return "<strong>И на Марсе будут яблони цвести!</strong>"


@app.route('/promotion_image')
def promote():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Яндекс!</title>
                      </head>
                      <body>
                        <h1>Привет, Яндекс!</h1>
                        <img src={url_for('static', filename='img/mars.png')}/>
                        {''.join([f'<div class="alert alert-{error}" role="alert">' + text + '</div>' for error, text in data])}
                      </body>
                    </html>'''
    # return '</br>'.join(data)


data = zip(["warning", "primary", "success", "danger"], ['Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!', 'Присоединяйся!'])

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')