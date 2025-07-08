# Homework-5
## Датасет был скачан и правильно распакован, правда на диске уже отформатированная версия.
## Первая попытка запустить example.py была безуспешна, так как изображения перед работой с ними не были переведены в тензоры, исправил файл и заработало
## вот последний этап из результатов выполнения example.py

![image](https://github.com/user-attachments/assets/9d379034-a191-4e4d-afb2-b318c67ffd10)

# Результат задания номер 1:
## Показываю результат применения только всех сразу, так как показ применения каждой аугментации к каждой картинке очень растянул бы отчёт
![image](https://github.com/user-attachments/assets/277e647a-9efa-4fbc-9ef2-72458bd56a69)
![image](https://github.com/user-attachments/assets/fda0ecac-0ae6-4a9a-9858-d2615279bda1)
![image](https://github.com/user-attachments/assets/0849df2d-7f90-4502-85c5-bd9964bde886)
![image](https://github.com/user-attachments/assets/4169f0dc-3e71-44c6-b9a4-82891ccfaf51)
![image](https://github.com/user-attachments/assets/9e4f4e34-e3dc-4a83-b9df-f2a93293bb1c)
![image](https://github.com/user-attachments/assets/5853429e-272f-406a-89b5-70268c60b2a8)

# Результат задания номер 2:

## 1)Случайная яркость
![image](https://github.com/user-attachments/assets/72ab8595-b281-4c74-af20-2b5c0a56ef10)

## 2)Мой блюр

![image](https://github.com/user-attachments/assets/568edbc7-61dc-42a2-8bb8-b2b74775a556)

## для сравнения вот результат гауссового шума из extra_augs

![image](https://github.com/user-attachments/assets/17d9e73d-71fa-4f12-9a2b-05f521cf8251)

## 3)Случайный контраст

![image](https://github.com/user-attachments/assets/a5f9fb22-c428-4bbb-ab61-de4f5d6c4c5b)
## Если сравнивать мои кастомные аугментации и аугментации и аугментации из extra_augs, то основным отличием будет то, что там настраиваются в основном вероятности срабатывания и пороговые значения (thresholds), а у меня регулируется интенсивность эффекта аугментации.

# Результат задания 3:
## Как мы можем видеть во всех классах одинаковое кол-во изображений, а именно 30 в каждом классе.
## распределение изображений по классам и общее распределение размеров:
![image](https://github.com/user-attachments/assets/662f855a-bdce-4316-a880-0bb41cd39c58)
## График ширины изображений:
![image](https://github.com/user-attachments/assets/c3916187-ba18-4bcf-bfb5-579ff27e6815)
## Распределение высот изображений(более равномерное):
![image](https://github.com/user-attachments/assets/d228cbf6-6634-4c30-9c75-3af99d3f6c4c)

# Результат задания 4:
## Я создал пайплайн позволяющий последовательно накладывать аугментации 
## Работа конфигурации light_config:

1)![image](https://github.com/user-attachments/assets/02c5c2e3-656d-4e0b-841a-a04de6145c06)
2)![image](https://github.com/user-attachments/assets/3a1547f2-ff5f-4772-85c5-4bc5090a8984)

## Работа конфигурации medium_config: в данном примере полегче даже лайта, но доделываю отчёт утром и менять времени нет

1)![image](https://github.com/user-attachments/assets/fe27c15f-aa99-4800-8c03-10bf19aaa5bf)
2)![image](https://github.com/user-attachments/assets/ed21b0b3-54d5-44c4-8346-b96e07cded0c)
3)![image](https://github.com/user-attachments/assets/84fe8b7f-4509-41ef-9ac7-9edb24750d79)

## Работа конфигурации heavy_config:

1)![image](https://github.com/user-attachments/assets/23542d9b-122e-440c-af3d-beca4fdfa5fd)
2)![image](https://github.com/user-attachments/assets/34b8750c-d634-45ea-a320-cd070c6b46da)
3)![image](https://github.com/user-attachments/assets/e57508eb-7b74-43ea-8a42-9463e7aa57ba)
4)![image](https://github.com/user-attachments/assets/f91a291d-9d23-466e-b84a-9d7ebcd56328)

## Вот как выглядят сами конфиги для пайплайнов:
## LIGHT
RandomBrightness((0.1, 1.1)))
RandomContrast((0.1, 1.05)))
## MEDIUM
RandomBrightness((0.8, 1.2))
RandomContrast((0.9, 1.1))
RandomBlur((1, 3))
## HEAVY
RandomBrightness((0.5, 10.5))
RandomContrast((0.7, 10.3))
RandomBlur((3, 10)))
Solarize(threshold=192)
# Результат задания 5:
## Как мы можем увидеть на примере 2 последовательных запусков программы графики времени обработки и потребления памяти нестабильны, но очевидно прослеживается общая тенденция к сильному увеличению времени обработки и требуемой памяти, но рост всё же не экспоненциальный
![image](https://github.com/user-attachments/assets/dff936cd-fbde-4a30-9178-b7ff6691beb5)
## Второй последовательный запуск
![image](https://github.com/user-attachments/assets/eef74633-b317-4419-85c0-ad53248aeb58)
## Пример самих значений (для 3 запуска программы, это не те же, что на графиках)
![image](https://github.com/user-attachments/assets/9de4488b-29f5-40d7-b37d-5b63f6fd9dae)


# Вывод:
## В ходе выполнения данного домашнего задания я потренировался в создании и применении аугментаций, которые на мой взгляд являются хорошим инструментом не только для создания новых данных на основе существющих, но и для улучшения качества работы моделей, также я подумал, что ,например, можно использовать аугментации как сложный тест для модели(заранее изменить изображение и посмотреть классифицирует ли модель его) и в какой момент аугментацию уже нельзя будет распределить в нужный класс, но для подобного нужно больше эксперементировать. В прошлом, при работе с проектами по компьютерному зрению у меня уже был опыт, можно сказать отмены аугментаций, когда изначально естественным образом аугментированное изображение нужно было приводить к стандартному виду. Было интересно снова поработать с этой темой. Извините за пропуск трёх работ (по личным обстоятельствам), постараюсь 6 и 7 домашками добрать баллы.
