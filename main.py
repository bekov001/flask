import os

from flask import Flask, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return "<strong>Миссия Колонизация Марса</strong>"


@app.route('/index')
def mission():
    return "<strong>И на Марсе будут яблони цвести!</strong>"


@app.route('/carousel')
def form_sample():
    script = """var myCarousel = document.querySelector('#myCarousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: 2000,
  wrap: true
})"""
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <title>Пейзажи</title>
                          </head>
                          <body>
                          <h1>Пейзажи</h1>
                          <div class="content">
                          <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
                          
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img src="{url_for("static", filename="img/mars1.jpg")}" class="d-block w-500px" alt="1">
                                </div>
                                <div class="carousel-item">
                                  <img src="{url_for("static", filename="img/mars2.jpg")}" class="d-block w-500px" alt="2">
                                </div>
                                <div class="carousel-item">
                                  <img src="{url_for("static", filename="img/mars3.jpg")}" class="d-block w-500px" alt="...">
                                </div>
                              </div>
                            </div>
                          </div>  
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
                          </body>
                        </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')