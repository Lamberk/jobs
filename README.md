# jobs
1. Клонируем проект (git clone https://github.com/Lamberk/jobs.git)
2. Устанавливаем зависимости (pip install -r requirements.txt)
3. Настраиваем базу. В данном случае используется MySQL, db_name = jobs_db, user = jobs, password = jobs (не забываем про миграции)
4. Запускаем manager command: `python manage.py get_superjobs`, которая через SuperJob API достанет компании, у которых есть вакансия "Продавец консультант" и создат для них объекты модели
5. Запускаем сервер (python manage.py runserver)
6. Можем посмотреть на компании, которые мы сохранили в базе по основному URL приложения. (http://127.0.0.1:8000/)
