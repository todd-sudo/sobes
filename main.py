def generator():
    for i in range(3):
        yield i


for i in generator():
    print(i)