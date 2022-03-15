# import hello
#
# print(hello.message("asd"))
# print(dir(hello))
# print(hello.__name__, hello.__file__)
# print(hello.__doc__)


def decorator_func(f, x, y):
    print("start of the decorator")

    def wrapper(t):
        t()
        print("end of the decorator")

    return wrapper


@decorator_func(1,2,3)
def simple():
    print("simple")


# simple = decorator_func(1, 2, 3)(simple)
