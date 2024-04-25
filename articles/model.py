import pickle
import os.path


class Article:  # хранит одну статью
    def __init__(self, title, author, pages, description):
        self.title = title
        self.author = author
        self.pages = pages
        self.description = description

    def __str__(self):
        return f'{self.title} ({self.author})'


class ArticleModel:  # хранятся все статьи
    def __init__(self):
        self.db_name = 'db.txt'
        self.articles = self.load_data()  # словарь со статьями

    def add_article(self, dict_article):  # сохраняет статью в словарь
        article = Article(*dict_article.values())
        self.articles[article.title] = article

    def get_all_articles(self):
        return self.articles.values()

    def get_single_article(self, user_title):
        article = self.articles[user_title]
        dict_article = {
            'название': article.title,
            'автор': article.author,
            'количество страниц': article.pages,
            'описание': article.description
        }
        return dict_article

    def remove_article(self, user_title):
        return self.articles.pop(user_title)

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.articles, f)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()
