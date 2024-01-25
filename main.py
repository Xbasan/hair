from flask import Flask, render_template, request

import json
import telebot


from post import post_assembly

bot = telebot.TeleBot('идентицыонный ключ бота')

app = Flask(__name__)

def sending_message(data):
    bot.send_message('id чата в виде числа',
                     f'ФИО: {data["fio"]}\n'
                     f'Название оргонизацыи: {data["organization"]}\n'
                     f'Описание Продукта или Услуги: {data["description"]}\n'
                     f'Контакты: {data["contact"]}\n'
                     f'Цена: {data["price"]}\n')



def hair_():
    return render_template('index.html')

def news_():
    news = post_assembly()
    return render_template('news.html', post=news)

def about_us_():
    return render_template('about_us.html')

@app.route('/news_js')
def news_html():
    return post_assembly()

@app.route('/',
           methods=['GET', 'HEAD', ])
def html_():
    html = request.args.get('html')

    if html is not None:
        match html:
            case 'app':
                return render_template('index.html')
            case 'news':
                return news_()
            case 'about_us':
                return about_us_()
            case _:
                return hair_()
    else: return hair_()
    
# ------------------------error------------------------------

@app.errorhandler(404)
def error_(e):
    with open('./templates/index.html',
              'rb') as file:
        response = file.read( )
    return response, 404, {"Content-Type": 'text/html'}

# -------------------------POST------------------------------

@app.route('/api2',
           methods=['POST', 'GET', ])
def api_json_():
    sending_message(request.get_json())
    json_response = {"server_status": 201, "description": 'request successfully corrected', }
    return json.dumps(json_response,
                      indent=2), 201, {"Content-Type": 'appliscation/json'}


# --------------------------------------------------------------

@app.route('/static',
           methods=['GET', 'HEAD', ])
def static_():
    publication = request.args.get('publication')
    publication_mp4 = request.args.get('publication_mp4')

    if publication is not None:
        with open('./static/publication/' + str(publication),
                  'rb') as file:
            response = file.read()
        return response, 201, {"Content-Type": 'img'}

    if publication_mp4 is not None:
        with open('./static/publication/' + str(publication_mp4),
                  'rb') as file:
            response = file.read()
        return response, 201, {"Content-Type": 'mp4'}


# --------------------------------------------------------------


if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0')  # 5000
