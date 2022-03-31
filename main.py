
# def bread(func):
#     def wrapper():
#         print()
#         func()
#         print("<\______/>")
#     return wrapper


# def ingredients(func):
#     def wrapper():
#         print("#помидоры#")
#         func()
#         print("~салат~")
#     return wrapper


# @bread
# @ingredients
# def sandwich(food="--ветчина--"):
#     print(food)


# sandwich()



class Shape:

    def calculate_area(self):
        raise NotImplemented


class Square(Shape):

    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):

    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


def get_area(input_obj):
    print(input_obj.calculate_area())


shape_obj = Shape()
square_obj = Square()
triangle_obj = Triangle()


# get_area(shape_obj)
get_area(square_obj)
get_area(triangle_obj)
