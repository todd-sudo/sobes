# Ответы на вопросы (собеседование)


1. ### ООП

    - `SOLID` 
        — это мнемоническая аббревиатура для набора принципов проектирования, 
        созданных для разработки программного обеспечения при помощи 
        объектно-ориентированных языков. Принципы SOLID направленны на 
        содействие разработки более простого, надежного и обновляемого кода.


        - `S` Single-responsibility principle 
            /Принцип единственной ответственности

            Его важность невозможно переоценить. 
            Каждый объект, класс и метод должны отвечать только за что-то одно
        
        
        - `O` Open–closed principle 
            / Принцип открытости-закрытости

            Программные объекты должны быть открыты для расширения, 
            но закрыты для модификации. Речь о том, что нельзя 
            переопределять методы или классы, просто добавляя 
            дополнительные функции по мере необходимости.

        - `L` Liskov substitution principle 
            / Принцип подстановки Лисков

            Этот принцип гласит, что объекты старших классов должны быть 
            заменимы объектами подклассов, и приложение при такой 
            замене должно работать так, как ожидается.

        - `I` Interface segregation principle 
            / Принцип разделения интерфейсов

            Объекты не должны зависеть от интерфейсов, которые они не используют
            Убедитесь, что вы не заставляете объекты реализовывать методы, 
            которые им никогда не понадобятся.

        - `D` Dependency inversion principle 
        / Принцип инверсии зависимостей

            Мы должны полагаться на абстракции, а не на конкретные реализации. 
            Компоненты ПО должны иметь низкую связность и высокую согласованность.


    - `YAGNI`
        You Aren’t Gonna Need It / Вам это не понадобится

        Этот принцип прост и очевиден, но ему далеко не все следуют. Если пишете код, то будьте уверены, что он вам понадобится. Не пишите код, если думаете, что он пригодится позже. 

    - `DRY`
        Don’t Repeat Yourself / Не повторяйтесь
    
    - `KISS`
        Keep It Simple, Stupid / Будь проще

    #### Инкапсуляция
    
    `Инкапсуляция` — ограничение доступа к методам и переменным.

    ``` python
    class B:
        def __private(self):
            print("Это приватный метод!")

    b = B()
    b.__private()

    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    AttributeError: 'B' object has no attribute '__private'



    class B:
        def _private(self):
            print("Это приватный метод!")

    b = B()
    b._private()


    $ >> Это приватный метод! 
    ```

    #### Наследование

    `Наследование` подразумевает то, что дочерний класс содержит все атрибуты
    родительского класса, при этом некоторые из них могут быть переопределены 
    или добавлены в дочернем

    #### Полиморфизм

    `Полиморфизм` - разное поведение одного и того же метода в разных классах.


2. ### Классы

    - `self` - ссылка на текущий созданный объект класса
    - `super()` - нужен для доступа к родительским классам


3. ### Типы данных в Python

    - изменяемые (списки, словари и множества)
    - неизменяемые (числа, строки и кортежи)
    - упорядоченные (списки, кортежи, строки и словари)
    - неупорядоченные (множества)


4. ### Генераторы и итераторы

    ```
    https://apirobot.me/posts/iterables-iterators-generators-in-python

    https://coderlessons.com/tutorials/python-technologies/
    
    izuchite-strukturu-dannykh-python/python-khesh-tablitsa
    ```

    `Итератор` – любой объект, реализующий метод `__next__`, который возвращает
    следующий элемент в очереди или выбрасывает исключение StopIteration, если не осталось элементов.

    `Итерируемый объект` – любой объект, реализующий метод `__iter__` или
     `__getitem__`. Итерируемым объектом является любая коллекция: список, кортеж, словарь, и т.д.

     `Цель итерируемого объекта` – создать итератор. Для этого у него есть метод
      `__iter__`, при каждом обращении к которому создается новый итератор.

    `Цель итератора` – пройтись по элементам. Для этого у него есть метод
     `__next__`, который возвращает элементы один за другим.

     ``` python
     
    items = [1, 2, 3]
    it = iter(items)

    while True:
        try:
            print(next(it))
        except StopIteration:
            break

    # >> 1
    # >> 2
    # >> 3

     ```

    `Генератор` – функция, которая генерирует значения. Она отличается от
    обычной функции тем, что может приостанавливать свое выполнение, возвращать
    промежуточный результат, а затем возобновлять выполнение в любой момент
    времени.

    ``` python

    def generator():
        for i in range(3):
            yield i


    for i in generator():
        print(i)

    # >> 0
    # >> 1
    # >> 2


    >>> # Вручную
    >>> gen = generator()
    <generator object generator at 0x7f38572b96d0>
    >>> next(gen)
    0
    >>> next(gen)
    1
    >>> next(gen)
    2
    >>> next(gen)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    StopIteration
    ```

    Генератор является итератором. Отличие итератора от генератора в том, что
    итератор извлекает элементы из коллекции (список, кортеж, …), а генератор
    может порождать элементы из воздуха.


5. ### Python — хэш-таблица

    `Хеш-таблицы` — это тип структуры данных, в которой адрес или значение
    индекса элемента данных генерируются из хеш-функции.
    Другими словами, в хэш-таблице хранятся пары ключ-значение, но ключ 
    генерируется с помощью функции хеширования.
    __Cами значения ключей становятся индексом массива__


6. ### Декораторы

    `Декоратор` - это функция, которая меняет поведение другой функции, не меняя ее код.

    ``` python
    def bread(func):
        def wrapper():
            print()
            func()
            print("<\______/>")
        return wrapper


    def ingredients(func):
        def wrapper():
            print("#помидоры#")
            func()
            print("~салат~")
        return wrapper


    def sandwich(food="--ветчина--"):
        print(food)


    sandwich = bread(ingredients(sandwich))
    sandwich()
    ```

    __Синтаксический сахар__

    ``` python
    def bread(func):
        def wrapper():
            print()
            func()
            print("<\______/>")
        return wrapper


    def ingredients(func):
        def wrapper():
            print("#помидоры#")
            func()
            print("~салат~")
        return wrapper


    @bread
    @ingredients
    def sandwich(food="--ветчина--"):
        print(food)


    sandwich()
    ```


7. ### Метаклассы, Абстрактные классы
    
    `Абстрактный класс` - в Python нет интерфейсов, это класс у которого нельзя создать объект. Он нужен для того чтобы создать контракт, который должны реализовать дочерние методы

    ``` python
    class User(ABC):

        @abstractmethod
        def create():
            pass
        
        @abstractmethod
        def update():
            pass
        
        @abstractmethod
        def delete():
            pass

        @abstractmethod
        def get():
            pass


    class CustomUser(User):
        
        def create():
            pass

        def update():
            pass

        def get():
            pass

        def delete():
            pass
    ```

    `Метаклассы` - шаблон для класса, на основе метакласса создаются классы, на основе класса строятся объекты. Для чего? Для того чтобы перехватить создание класса и его как-то изменить (или изм его состояние)


    ``` python
    class Meta(type):
        """Мета класс"""
        def __new__(cls, name, bases, attrs):
            attrs["my_field"] = "Value"
            return super().__new__(cls, name, bases, attrs)


    class User(metaclass=Meta):
        def __init__(self) -> None:
            print("Конструктор")
            super().__init__()


    u = User()
    print(u.my_field)

    $ >> Конструктор
    $ >> Value

    ```



8. ### Базы данных

    - NoSQL (Mongo, Redis)

    - SQL (Postgres, MySQL)

        - Связи(3) - реализация
            - `Многие ко многим.`
                ``` sql
                PRAGMA foreign_keys=on;
                
                CREATE TABLE books(
                    Id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    count_page INTEGER NOT NULL CHECK (count_page >0),
                    price REAL CHECK (price >0)
                );
                
                CREATE TABLE auth(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER  CHECK (age >16)
                );
                
                CREATE TABLE auth_book (
                    auth_id INTEGER NOT NULL,
                    books_id INTEGER NOT NULL,
                    FOREIGN KEY (auth_id) REFERENCES auth(id)
                    FOREIGN KEY (books_id) REFERENCES books(id)
                );
                ```
            - `Один ко многим.`

                ``` sql
                PRAGMA foreign_keys=on;
                
                CREATE TABLE books(
                    Id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    count_page INTEGER NOT NULL CHECK (count_page >0),
                    price REAL CHECK (price >0),
                    auth_id INTEGER NOT NULL,
                    FOREIGN KEY (auth_id) REFERENCES auth(id)
                );
                
                CREATE TABLE auth(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER  CHECK (age >16)
                );
                ```
            - `Один к одному.`
        - Запросы

            #### - `INNER JOIN (Внутреннее соединение)` - предназначен для соединения двух или более таблиц базы данных по совпадающему условию.
                
            Объединяет поля строки из одной таблицы с полями другой, если выполняется условие, 
            что покупатель товара (family_member) совпадает с идентификатором члена семьи (member_id):

            ```sql 
                SELECT * FROM Payments  JOIN FamilyMembers ON family_member = member_id;
            ```

            #### - `LEFT OUTER JOIN (Внешнее левое соединение)`

            В выборку попадают все строки из левой таблицы, дополненные данными о занятиях.

            #### - `(RIGHT OUTER JOIN Внешнее правое соединение)`

            Соединение, которое возвращает все значения из правой таблицы, соединённые с соответствующими 
            значениями из левой таблицы если они удовлетворяют условию соединения, или заменяет их на NULL в обратном случае.

            #### - ` FULL OUTER JOIN (Внешнее полное соединение)`

            Соединение, которое выполняет внутреннее соединение записей и дополняет их левым внешним соединением и правым внешним соединением.

            #### - `Оператор SQL HAVING`

            является указателем на результат выполнения агрегатных функций. Агрегатной функцией в языке 
            SQL называется функция, возвращающая какое-либо одно значение по набору значений столбца. 
            Такими функциями являются: `SQL COUNT(), SQL MIN(), SQL MAX(), SQL AVG(), SQL SUM()`.

            ```sql
            SELECT Singer, SUM(Sale) # выбирает исполнителей и число продаж
            FROM Artists # из таблицы Артисты
            GROUP BY Singer
            HAVING SUM(Sale) > 2000000 # когда число продаж больше 2000000
            ```

            `Вывод:`
            ```sql
            Singer 	        Sum(Sale)

            Massive Attack 	54000000
            The Prodigy 	33000000
            ```


            Выводит название исполнителя, который исполнялся еще до 1995 года
            ```sql
            SELECT Singer, MIN(Year)
            FROM Artists
            GROUP BY Singer
            HAVING MIN(Year) < 1995
            ```

            `Вывод:`
            ```sql
            Singer 	        MIN(Year)

            The Prodigy 	1994
                ```

            

        - Индексы

            Индексы нужны, если мы часто используем какие-либо поля, мы назначаем индекс этому полю

        - Триггеры
        - Транзакции
        - ACID (википедия)
        - Уровни изолированности транзакции(4) (+-)


9. ### Docker

    - Чем отличается докер от виртуальной машины
    - image - образ 
    - container - запущенный экземляр
    - volume - когда останавливается контейнер, внутри него все уничтожается(все что наработалось), поэтому нам нужны volume чтобы работало
    - register - хранилище для готовых изображений
    - Dockerfile, .dockerignore
    - docker-compose - нужен для того чтобы поднять инфраструктуру проекта(зависимости сервисов)



10. ### WEB

    - REST - набор архитектурных принципов построения сервис-ориентированных систем.

    - RESTful - прилагательное, употребляющееся по отношению к сервисам, которые следуют принципам REST. Чем больше принципов требований вы выполните тем более `full` будет приложение

    - Требования к архитектуре REST:
        - Модель клиент-сервер
        - Отсутствие состояния - никакая информация о состоянии клиента на сервере не хранится "Stateless protocol" 
        - Кэширование - способно частично или полностью устранить некоторые клиент-серверные взаимодействия, ещё больше повышая производительность и масштабируемость системы
        - Единообразие интерфейса - позволяют каждому из сервисов развиваться независимо. 
        - Слои - сервера, масштабируемость
        - Код по требованию
