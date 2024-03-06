import os

files_in_directory = os.listdir('./static/publication')


def description_(file, description):
    with open(f'./static/publication/{file}/{description}', 'r', encoding='utf-8') as file:
        response = file.read()
    return response


def post(file):
    _img_arr = []
    _vidio_arr = []
    _description = ''

    publication_num = os.listdir(f'./static/publication/{file}')
    for i in publication_num:
        if i.endswith(('jpg', 'png')):
            _img_arr.append(i)
        elif i.endswith(('mp4', 'mov')):
            _vidio_arr.append(i)
        elif i.endswith('txt'):
            _description = description_(file, i)

    return {
        'image': _img_arr,
        'video': _vidio_arr,
        'description': _description,
    }


def post_assembly():
    news = {}
    for file in files_in_directory:
        news[f'{file}'] = post(file)

    return news


if __name__ == '__main__':
    print(post_assembly())
