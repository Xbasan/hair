import os

files_in_directory = os.listdir('./static/publication')

def publication_(type,file, publication_,slide_img_num,slide_num,):
    #  <{type} class="slide_img_{slide_img_num} slide{slide_num}" src="{{url_for('static', publication='{file}/{publication_}')}}" alt="Чето не так" />
    return f'''<{type}   class="slide_img_{slide_img_num} slide{slide_num}" src="./static?publication={file}/{publication_}" alt="Чето не так" controls>\n'''

def slide_(slide,btn_num):
    return f'''
        <div class="publication">\n
            {slide}
        </div>\n
        <div class="button_slider">\n
            <button id="post_{btn_num}_left" class="left button_s"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAUElEQVR4nO2UsQnAMAwET5tlomSVpPO0jhsFjHH7wYY/UPsHEnowZkLkSAjgAYpCEhn+AhU4lOGnw+Vr+QR3J7gQEJYs82jjTSRV8UvZmQ1pR+wf4JpfHEcAAAAASUVORK5CYII="></button>\n
            <button id="post_{btn_num}_right" class="right button_s"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAS0lEQVR4nO2UsQ0AIQwDL5uxTdbhO6YFmhQsYD1IPiltTolkgzFF1EgI4AOGStKACawSSSR5SGSXpCVXvCq9/JegBdCVAZOXnXmcDdAZH+AfKMBTAAAAAElFTkSuQmCC"></button>\n
        </div>\n
        '''

def description_(file,description):
    with open(f'./static/publication/{file}/{description}', 'r',  encoding='utf-8') as file:
        response = file.read()
    return response


def post_assembly():
    news = ''
    i = 1
    for file in files_in_directory:
        publication = ''
        publication_img = os.listdir(f'./static/publication/{file}')
        j = 1
        for post_file in publication_img:
            if post_file.endswith(('jpg', 'png')):
                publication += publication_('img',
                                            file,
                                            post_file,
                                            i,
                                            j)
                j +=1
            elif post_file.endswith('mp4'):
                publication += publication_('video',
                                            file,
                                            post_file,
                                            i,
                                            j)
                j += 1
            else:
                description = description_(file,post_file)
        news += (f'<div class ="post post_{i}">\n'
                 f'<div class="slider">\n{slide_(publication, i)}\n</div>\n'
                 f'<div class="description">\n'
                 f'<p class="description_p">{description}</p>\n'
                 f'</div>\n'
                 f'</div>\n')
        i+=1
    return f'<div class="news">{news}</div>'




if __name__ == '__main__':
    print(post_assembly())
