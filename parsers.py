# import requests
# from bs4 import BeautifulSoup
#
#
# # мы вынесли сюда часть файлов что бы сделать парсер в ООП ,с классом
#
#
# class Parser:
#     html = ''  # это будет экземпляр BeautifulSoup
#     res = []  # сюда попадают все собранные данные
#
#     def __init__(self, url, path):  # тут принимается путь по которому будем парсить
#         # , и название документа куда мы эти данные будем сохранять
#         self.url = url
#         self.path = path
#
#     # тут получаем доступ ко всей нашей разметке
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     # сделаем метод где будем получать данные - парсить
#     # получим описание под картинкой  .
#     def parsing(self):
#         news = self.html.find_all('div', class_='caption')
#         # так как дивов получится много с таким классом применим цикл и будем искать заголовок с h3 который есть не везде
#         for item in news:
#             title = item.find('h3').text  # доступ к заголовкам
#             # print(title)
#             href = item.find('h3').find('a').get('href')  # доступ к ссылке
#             # print(href)
#             author = item.find('a', class_='topic-info-author-link').text.strip()  # доступ к автору статьи
#             # print(author)
#             self.res.append({  # список с нашими переменными в которых доступ к данным (с возможностью добавления)
#                 'title': title,
#                 'href': href,
#                 'author': author
#             })
#         # print(self.res)  # принт находится под фор (отрабатывает когда закончится фор)
#
#     # метод сохранения данных в текстовый файл пройдемся по списку с нашими данными
#     # при каждой итерации выводится одна новость и происходит след итерация где выводится след новсть .
#     def save(self):
#         with open(self.path, 'w') as file:
#             i = 1  # номер новости
#             for item in self.res:
#                 file.write(
#                     f'Новость № {i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\nАвтор: {item["author"]}'
#                     f'\n\n{"*" * 30}\n'
#                 )
#                 i += 1
#
#     # это метод вызывающий поочередно все методы по очереди парсинка сайта
#     def run(self):
#         self.get_html()
#         self.parsing()
#         self.save()


import requests
from bs4 import BeautifulSoup


# мы вынесли сюда часть файлов что бы сделать парсер в ООП ,с классом


# class Parser:
#     html = ''  # это будет экземпляр BeautifulSoup
#     res = []  # сюда попадают все собранные данные
#
#     def __init__(self, url, path):  # тут принимается путь по которому будем парсить
#         # , и название документа куда мы эти данные будем сохранять
#         self.url = url
#         self.path = path
#
#     # тут получаем доступ ко всей нашей разметке
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     # сделаем метод где будем получать данные - парсить
#     # получим описание под картинкой  .
#     def parsing(self):
#         news = self.html.find_all('div', class_='caption')
#         # так как дивов получится много с таким классом применим цикл и будем искать заголовок с h3 который есть не везде
#         for item in news:
#             title = item.find('h3').text  # доступ к заголовкам
#             # print(title)
#             href = item.find('h3').find('a').get('href')  # доступ к ссылке
#             # print(href)
#             author = item.find('a', class_='topic-info-author-link').text.strip()  # доступ к автору статьи
#             # print(author)
#             self.res.append({  # список с нашими переменными в которых доступ к данным (с возможностью добавления)
#                 'title': title,
#                 'href': href,
#                 'author': author
#             })
#         # print(self.res)  # принт находится под фор (отрабатывает когда закончится фор)
#
#     # метод сохранения данных в текстовый файл пройдемся по списку с нашими данными
#     # при каждой итерации выводится одна новость и происходит след итерация где выводится след новсть .
#     def save(self):
#         with open(self.path, 'w') as file:
#             i = 1  # номер новости
#             for item in self.res:
#                 file.write(
#                     f'Новость № {i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\nАвтор: {item["author"]}'
#                     f'\n\n{"*" * 30}\n'
#                 )
#                 i += 1
#
#     def run(self):
#         for i in range(1, 5):
#             self.url + f'page{i}/'
#             self.get_html()
#             self.parsing()
#             self.save()

    # это метод вызывающий поочередно все методы по очереди парсинка сайта
    # def run(self):
    #     self.get_html()
    #     self.parsing()
    #     self.save()
