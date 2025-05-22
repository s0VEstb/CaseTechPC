### Рукаводство по работе

1. Клон
   ```sh
   git clone https://github.com/s0VEstb/CaseTechPC.git
   ```
2. Создание виртуальной среды (venv/.venv)
   ```sh
   python -m venv <name>
   ```
3. Установка зависимостей
   ```sh
   pip install -r requirements.txt
   ```
4. Создание файла .env (не подходит для продакшн)
   просто создаешь этот файл и вставляешь это:
   ```sh
   SECRET_KEY=django-insecure-%fgh44u269__z3@o#w!ya^+#6tp057l&#4k=y$+@ifrajnih-+
    DEBUG=True
    PROD=False
   ```
5. Oткрой ветку с названием своего таска и перейди в нее
   ```sh
   git checkout -b <name>
   ```

6. Что бы взять изменения с ветки dev
   ```sh
   git pull origin dev
   ```

7. Соблюдайте принцип "Convertional Commit"
   три вида:
     -fix (eсли исправили что-то)
     -feat (если добавили новый функционал)
     -refactor (eсли изменили рассположение чего-то в коде)
   пример:
   ```sh
   "fix: fixed api of url about_us"
   "feat: added search for project"
   "refactor: moved model of room ahead of model info"
   ```
   если что можете гибрид делать типо:
   ```sh
   "fix-feat:
    fix-refactor:
    и тд"
   ```