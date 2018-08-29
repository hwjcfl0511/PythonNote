'''
定义一个类
'''
class Student():
    pass

mingyue = Student()

class PythonStudent():
    name = None
    age = 18
    course = "Phthon"
    def doHomework(self):
        print("我在做作业")
        return None

yueyue = PythonStudent()
yueyue.name="小岳岳"
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()