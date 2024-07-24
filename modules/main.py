import library as lb
import test_func as tf

def printer():
    print(x)

def modifier():
    global x
    x += 10
    print(x)


print('main module')
lb.foo(3)
lb.foo(5)
x = lb.bar(1, 5)
print(x)

lb.create_object('Круг1')
lb.create_object('Круг2')
lb.create_object('Круг3')
lb.print_objects()

for obj in lb.objects:
    if 'Круг1' in obj:
        print('Найден круг 1!')
lb.objects.pop()
lb.print_objects()

printer()

z = tf.summer(1, 2)
print(z)