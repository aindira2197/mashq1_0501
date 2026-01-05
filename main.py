class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"Ism: {self.name}, Yosh: {self.age}, Baho: {self.grade}")


# Obyektlar
s1 = Student("Ali", 20, 90)
s2 = Student("Vali", 21, 85)

s1.info()
s2.info()
