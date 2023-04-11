# Test-Python
Опис проекту
Цей проект є прикладом автоматизації веб-тестування з використанням мови програмування Python і фреймворку Selenium із реалізацією шаблону Page Object.

Встановлення
1. Встановіть Python 3.x з офіційного сайту 
[https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Завантажте або клонуйте проект з GitHub
3. Перейдіть до папки з проектом у терміналі
4. Створіть та активуйте віртуальне середовище за допомогою команд:
```
python -m venv venv
```
```
venv\Scripts\activate
```
(для Windows)
```
source venv/bin/activate
```
(для Linux/MacOS)

5. Встановіть всі залежності проекту, виконавши команду 
```
pip install -r requirements.txt
```

Запуск
1. Відкрийте термінал та перейдіть до папки з проектом
2. Запустіть тестовий файл за допомогою команди
```
pytest test_file.py, де test_file.py
```
- назва файлу з тестами.
3. Чи використайте команду для всіх тестів
```
python -m pytest tests/
```

Структура проекту
tests: директорія з тестами
pages: директорія з класами сторінок
helpers: директорія з допоміжними класами та методами
conftest.py: файл з налаштуваннями PyTest

Test-Python
Project Description
This project is an example of web testing automation using Python programming language and Selenium framework with the Page Object pattern implementation.

Installation

1. Install Python 3.x from the official website
[https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download or clone the project from GitHub
3. Navigate to the project folder in the terminal
4. Create and activate a virtual environment with the following commands:
```
python -m venv venv
```
```
venv\Scripts\activate
```
(for Windows)
```
source venv/bin/activate
```
(for Linux/MacOS)

5. Install all project dependencies by executing the command
```
pip install -r requirements.txt
```

Usage

1. Open the terminal and navigate to the project folder
2. Run the test file using the command
```
pytest test_file.py
```
, where test_file.py is the name of the file with tests.
3. Alternatively, run all tests using the command
```
python -m pytest tests/
```
