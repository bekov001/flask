from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "<strong>Миссия Колонизация Марса</strong>"


@app.route('/index')
def mission():
    return "<strong>И на Марсе будут яблони цвести!</strong>"


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
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
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input class="form-control" placeholder="Введите фамилию">
                                    <input class="form-control" placeholder="Введите имя">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <label for="classSelect">Ваше образование</label>
                                    <select class="form-select">
                         
                                      <option>Начальное</option>
                                      <option>Среднее</option>
                                        <option>Высшее</option>
                                    </select>
                                    <label for="check">Ваша проффесия</label>
                                    <div id="check">
                                    {"<br/>".join([f'<input type="checkbox" id="{el}"/> <label class="form-check-label" for="{el}">{el}</label>' for el in data])}
                                    </div>
                    
                                    <div class="form-group">
                                        <label for="about">почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли вы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


data = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
       'инженер по терраформированию', 'климатолог',
       'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
       'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода',
       'киберинженер', 'штурман', 'пилот дронов'] 
 

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')