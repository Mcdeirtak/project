# Кейсове завдання Software engineering school
### Результатом виконання завдання є консольний додаток написаний мовою програмування Python(консольний додаток було розроблено через неможливість ознайомлення з розробкою додатків для виклику їх через запити). Робота виконана студентами Національного Авіаційного Університету, Бойко Владиславом Миколайовичем та Косованом Михайлом Михайловичем.
____
 В ході виконання кейсового завдання було:
- Написано роботу з API, а саме:
    - Завантажено та підключено до проекту фреймворк для роботи з API
    - За допомогою стороннього сервісу отримано курс BTC в USD
    - Переведено курс в UAH за допомогою національного банку України
    - Виконано запуск на локальному сервері
- Виконано роботу з підпискою для отримання курсу BTC на email:
    - Використано regular expression для перевірки правильності введеного користувачем email
    - При правильному введенні та відсутності введеного email у файловій базі данних, email записується в файл
    - При будь-якій помилці виводиться відповідне повідомлення про помилку
- Останнім кроком написання програми було розроблення розсилки повідомлень з курсом на вказані email:
    - Для початку було отримано дані з файлової бази
    - Далі було підключено бібліотеки для отримання поточної дати та взято з першого програмного файлу дані про курс
    - Підключено сервер для роботи з повідомленнями на gmail.com(саме з цього сервісу будуть відправлятися повідомлення)
    - Створено email для відправки повідомлень
    - Створено функцію для розсилки:
        - Виконується відправка повідомлення на адресу
        - При помилці записується почта в новий список, який потім буде записано у файл
        - В будь-якому випадку з файлу видаляється записаний раніше email
        - У файл записуються email, на які не вдалося відправити повідомлення
____
### Для роботи додатка потрібно встановити Python v 3.6+ та завантажити модулі(flask, flask_restful, requests) за допомогою команди: "pip install {Module name}" в терміналі.