# Система управління бібліотекою

## Опис
Модульна система для автоматизації роботи бібліотеки: облік книг, видача/повернення, сповіщення читачів. Проєкт розроблено в рамках лабораторних робіт з КПЗ.

## Встановлення та запуск
```bash
git clone [https://github.com/Ve1izar/Dlabs.git](https://github.com/Ve1izar/Dlabs.git)
cd library-system
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
## Тестування
```bash
python -m unittest discover tests/
```
Автор: Стадницький Даніеле, група ІПЗ-32