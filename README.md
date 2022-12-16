# Basic text preprocessing service for NLP tasks
Функциональные требования:
https://docs.google.com/spreadsheets/d/e/2PACX-1vTKFJyti4QLHsscOlGAzsBm6SmILgtVAQXzyVRGrT5moYzsHUTMlQi0QKxiOQPC_Z-C9nWgGeOrKYPM/pubhtml

## Установка
	pip3 install -r requirements.txt
	pip3 install .

## Запуск
	streamlit run preprocessor/preprocess.py

После запуска будут указаны Network и External URL адреса приложения.
## Docker
### Сборка
	docker build -t preprocessor .
### Запуск
	docker run preprocessor

## Демонстрация работы
![example](/img/example.png)

## Тесты
Main: [![tests pass status](https://github.com/nikiens/SELabs/actions/workflows/tests.yml/badge.svg?branch=main)](https://https://github.com/nikiens/SELabs/actions/workflows/tests.yml)
Develop: [![tests pass status](https://github.com/nikiens/SELabs/actions/workflows/tests.yml/badge.svg?branch=develop)](https://github.com/nikiens/SELabs/actions/workflows/tests.yml)