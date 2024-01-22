import json
import socket
import telebot

bot = telebot.TeleBot('5473853379:AAGy2mEkaKNlLmOS2r4kIZxbVVxhC-LxnQQ')


def sending_message(data):
    message_object = json.loads('{' + data.split('{')[1])
    bot.send_message(-1001815673799, f'ФИО: {message_object["fio"]}\n'
                                     f'Название оргонизацыи: {message_object["organization"]}\n'
                                     f'Описание Продукта или Услуги: {message_object["description"]}\n'
                                     f'Контакты: {message_object["contact"]}\n'
                                     f'Цена: {message_object["price"]}\n')


def start_server():
    try:
        server = socket.socket(socket.AF_INET,
                               socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 2000))
        server.listen(40)
        print(f'____________________________________\n'
              f'|卐|       Cервер запущен       |卐|\n'
              f'|卐|     Server is running      |卐|\n'
              f'|卐|       Негры не люди        |卐|\n'
              f'|卐|   http://127.0.0.1:2000/   |卐|\n'
              f'¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        while True:
            client_socket, address = server.accept( )
            data = client_socket.recv(1024).decode('utf-8')
            content = load_page_from_get_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close( )
        print(f'____________________________\n'
              f'|卐| The server crashed |卐|\n'
              f'|卐|    Сервер упал     |卐|\n'
              f'¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n')


def load_page_from_get_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
    HDRS_CSS = 'HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=utf-8\r\n\r\n'
    HDRS_JS = 'HTTP/1.1 200 OK\r\nContent-Type: text/js; charset=utf-8\r\n\r\n'
    HDRS_IMG = 'HTTP/1.1 200 OK\r\nContent-Type: img; charset=utf-8\r\n\r\n'

    print(request_data)

    path = request_data.split(' ')[1]
    path_img = path.split('/')[1]
    print(path_img)

    response = ''
    if request_data.split(' ')[0] == 'GET':
        match path:
            case '/hair':
                with open('templates/index.html',
                          'rb') as file:
                    response = file.read( )
                return HDRS.encode('utf-8') + response
            case '/news':
                with open('templates/news.html',
                          'rb') as file:
                    response = file.read( )
                return HDRS.encode('utf-8') + response
            case '/css/style.css':
                with open('templates/css/style.css',
                          'rb') as file:
                    response = file.read( )
                return HDRS_CSS.encode('utf-8') + response
            case '/js/scripr.js':
                with open('templates/js/scripr.js',
                          'rb') as file:
                    response = file.read( )
                return HDRS_JS.encode('utf-8') + response
            case '/js/slider.js':
                with open('templates/js/slider.js',
                          'rb') as file:
                    response = file.read( )
                return HDRS_JS.encode('utf-8') + response
            case _:
                if path.split('/')[1] == 'static':
                    with open('./templates' + path, 'rb') as file:
                        response = file.read()
                    return HDRS_IMG.encode('utf-8') + response
                else:
                    with open('./templates' + '/index.html',
                              'rb') as file:
                        response = file.read( )
                    return HDRS.encode('utf-8') + response
    elif request_data.split(' ')[0] == 'POST':
        sending_message(request_data)
        return f'True'.encode('utf-8')
    else:
        return f'False'.encode('utf-8')


if __name__ == '__main__':
    start_server( )
