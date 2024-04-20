# тут первый запуск проги,из модуля controller делаем импорт класса Controller
from controller import Controller


def main():
    app = Controller()  # создадим экземпляр и будем вызывать у него метод
    app.run()


if __name__ == '__main__':  # укажем что def main() будет запускаться только если запуск идет с этого документа
    main()
