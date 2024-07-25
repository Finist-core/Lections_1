
class Student:
    def __init__(self, name, age): #init - конструктор, все параметры вносить в них
        self.name = str(name)
        self.age = int(age)
        print('Студент', name, age, 'лет', 'внесен в БД')
        #init может быть только один на один класс, в коде может быть не один

name = str(input("Введите имя студента: ")) #Почему даёт ввести цифры???
age = int(input("Введите возраст студента: "))

student = Student(name, age)

#Student2 = Student() #тут будет ошибка, так как нет параметров
#Student1 = Student('Вася', 17) #в скобках параметры конструктора
#Student3 = Student('Петя', 20)
#Student4 = Student(10, 10) #ВОПРОС: почему не ругается???

#print(dir(Student)) #dir показывает пространство имен
#Student()



