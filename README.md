#Распознавание жестов с помощью MobileNet и Raspberry
##Задание
Подключить 1 lcd1602 экран, 1 кнопку. Реализовать распознавание жестов (3-5 разных жестов). На lcd экран выводить распознанные жесты.
##Выполнение
Нейронная сеть MobileNet является сложной свёрточной сетью, которая предварительно обучена на большом наборе данных. Предварительное обучение на большой выборке открывает возможность реализовать transfer learning – метод, при котором используются полученные ранее веса и связи, но без верхних уровней, вместо которых обучаются новые на наборе данных для необходимой задачи. Подробно алгоритм описан в гайде “Transfer learning and fine-tuning” от TensorFlow [1].
Для обучения был использован датасет Hand Sign Recognition (ASL) [2], представляющий из себя контрастные контуры фотографий американского языка жестов, размером 64 на 64 пикселя. Для корректного распознавания с фотографий удалён фон, а сами руки преобразованы с крайне высокой контрастностью, в результате чего на фотографии виден только силуэт, что уменьшает объём данных, который нужно обработать.


##Алгоритм работы с программой
Для корректной работы сети необходимо выполнить следующий алгоритм:
1)	Запустить скрипт распознавания rec.py;
2)	Установить камеру таким образом, чтобы в прямоугольник образовался затемнённый фон. Идеальным вариантом будет подсветка рассеянным светом на фоне далеко стоящей стены;
3)	Зафиксировать фон без руки, нажатием клавиши b. О результате можно судить по сообщению и потемневшему окну 2;
4)	В случае неудачной фиксации нажать клавишу r и повторить предыдущий пункт;
5)	По нажатию клавиши пробел будет зафиксировано изображение в прямоугольнике, распознан жест, а результат выведен в поток вывода и окно 3 с подписью жеста;
6)	Для завершения работы нажать Esc.

##Отличия при работе на плате
Для управления дисплеем использована шина I2C. После запуска скрипта на Raspberry необходимо нажать три раза кнопку. После третьего нажатия активируется камера и начинается код, аналогичный rec.py. После получения результата, вывод анализируется на экран с помощью модуля управления экраном выводится буква, символ которой распознан.

##Выводы
В данной работе были изучены основы работы с Raspberry, Raspbian, GPIO и внешней периферией. Была изучена нейронная сеть MobileNet, переобучена и реализована на микрокомпьютере. В ходе выполнения работы были вновь пройдены темы обучения нейронных сетей, обработки изображений, правил подключения периферии к плате и изучены новые модули.
##Ссылки
1.	Transfer learning and fine-tuning // TensorFlow Core URL: https://www.tensorflow.org/tutorials/images/transfer_learning (дата обращения: 01.10.2020).
2.	Hand Sign Recognition // Kaggle URL: https://www.kaggle.com/bikashpandey17/hand-sign-recognition (дата обращения: 01.10.2020).

