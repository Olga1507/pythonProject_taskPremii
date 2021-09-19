# pythonProject_taskPremii
Условие задачи

Ограничение времени, с 1
Ограничение памяти, МБ 64
Общее число попыток отправки 15

Петр Васильевич, директор ОАО "Рога и рога", собирается раздать премию всем менеджерам компании, он добрый и честный человек, поэтому хочет соблюсти следующие условия:

премия должна быть равной для всех менеджеров
должна быть максимально возможной и целой
должна быть выдана одной транзакцией с одного счета для каждого менеджера, без использования нескольких счетов для отправки одной премии

У Петра Васильевича открыто N корпоративных счетов, на которых лежат разные суммы денег Cn, а в компании работает M менеджеров.
Необходимо выяснить максимальный размер премии, которую можно отправить с учетом условий. Если денег на счетах компании не
хватит на то, чтобы выдать премию хотя бы по 1 у.е. - значит премии не будет, и нужно вывести 0.


Входные данные (поступают в стандартный поток ввода)
Первая строка - целые числа N и M через пробел (1≤N≤100 000, 1≤M≤100 000)

Далее N строк, на каждой из которых одно целое число Cn (0≤Cn≤100 000 000)

Проверка входных данных и обработка неправильных данных на входе не нужна, тестовые данные для проверки гарантированно подходят под описание выше


Выходные данные (ожидаются в стандартном потоке вывода)
Одно целое число, максимально возможная премия


Пример 1
Ввод:

4 6
199
453
220
601
Вывод:

200

Пример 2
Ввод:

2 100
99
1
Вывод:

1

Пример 3
Ввод:

2 100
98
1
Вывод:

0
