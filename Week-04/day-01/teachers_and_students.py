class Student(object):
    def learn(self):
        pass

    def question(self):
        Teacher.answer(self)

class Teacher(object):
    def teach(self):
        pass

    def answer(self):
        Student.learn(self)