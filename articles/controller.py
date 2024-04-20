from view import UserInterface
from model import ArticleModel


class Controller:
    def __init__(self):
        self.article_model = ArticleModel()  # для доступа к другим модулям
        self.user_interface = UserInterface()  # view

    def run(self):  # запускает работоспособность нашей программы
        # создадим цикл пока то что введет пользователь не будет означать выход из программы
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()  # ввод текста пользователем
            self.check_user_answer(answer)

    def check_user_answer(self, answer):  # ответы пользователя
        if answer == '1':
            article = self.user_interface.add_user_article()  # добавление статьи(данные в статье)
            self.article_model.add_article(article)
        elif answer =='2':
            articles = self.article_model.get_all_articles()
            self.user_interface.show_all_articles(articles)
        elif answer == '3':
            article_title = self.user_interface.get_user_article()
            try:
                article = self.article_model.get_single_article(article_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title)
            else:
                self.user_interface.show_single_article(article)
        elif answer == '4':
            article_title = self.user_interface.get_user_article()
            try:
                title = self.article_model.remove_article(article_title)
            except KeyError:
                self.user_interface.show_incorrect_title_error(article_title)
            else:
                self.user_interface.remove_single_artile(title)
        elif answer == 'q':
            pass
        else:
            self.user_interface.show_incorrect_answer_error(answer)






