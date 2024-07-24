objects = []

def foo(x):
    print('foo', x)

def bar(a, b):
    #функциия складывает и возращает a+b
    return a + b

def create_object(name):
    objects.append('object[' + name + ']')

def print_objects():
    print('Все добавленные объекты')
    for obj in objects:
        print(obj)
if __name__ == '__main__':
    print('Library executed separatly.')
    print('Lets test it self')

    if bar(2, 2) == 4:
        print('OK')
    else:
        print('FAIL')