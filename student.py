class Student:
    """ a class for Student
    """

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    # no need for a method since there are no other inputs and no new action, it's a property
    @property
    def average(self):
        if len(self)>0:
            return sum(self.marks)/len(self.marks)
        else:
            return None

# an example of a magic method
    def __len__(self):
        return len(self.marks)

    def __getitem__(self, x):
        return self.marks[x]

    def __repr__(self):
        return f'<Student {self.name} {self.school}>'

    def __str__(self):
        return f'Student {self.name} with {len(self)} grades'


class WorkingStudent(Student):
    """
    A subclas of Student for Working student
    """
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    # weekly_salary is not a function, it operates on existing properties
    @property
    def weekly_salary(self):
        return self.salary * 37.5


student_one = Student('Ana', 'First High')
student_two = WorkingStudent('Maria', 'Second High', 12)

print(student_two.name)
print(student_two.school)
print(student_two.salary)
student_two.marks.append(11)
student_two.marks.append(13)
print(student_two.average)
print(student_two.weekly_salary)
print(student_two)


print(student_one.name)
student_one.marks.append(12)
student_one.marks.append(10)
print(student_one.average)
print(len(student_one))
print(student_one[0])

for g in student_one:
    print(g)


print(student_one)
