class B:
    def _private(self):
        print("Это приватный метод!")

b = B()
b._private()