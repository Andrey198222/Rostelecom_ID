Итоговый проект по автоматизированному тестированию функционала страницы https://b2c.passport.rt.ru сайта "Ростелеком"
При тестировании сайта были написаны:

    ручные чек-лист и тест-кейсы;
    баг-репорты;
    автоматизированные тесты
    Было проведено автоматизированное тестирование с использованием Selenium и PyTest: 1.В корневой папке находятся файлы settings.py с тестовыми данными, chromedriver.exe, requirements.txt 2.Папка Тests содержит файлы для запуска автотестов: • tests_pages.py - тесты для страниц авторизации, регистрации и восстановление пароля, • tests_input_field.py - тесты для полей ввода. Запуск тестов осуществляется с помощью команд из консоли: • pytest -v --driver Chrome --driver-path Git\Rostelecom\chromedriver.exe Tests\tests_pages.py,
• pytest -v --driver Chrome --driver-path Git\Rostelecom\chromedriver.exe Tests\tests_input_field.py
• или кнопкой Run Pycharm
