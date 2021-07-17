# xargs
def student(*details):
    print(details)


student(1)  # (1,) Like Tuples
student(1, 2, "Hasan")  # (1, 2, 'Hasan')


def add(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    return result


print(add(1, 2, 3, 4, 5))  # 15


# xxargs
def student(id, name):
    print(id, name)


def studentV2(**details):
    print(details["name"])


student(id=10, name="Hasan")  # 10 Hasan
studentV2(id=10, name="Hasan")  # Hasan
