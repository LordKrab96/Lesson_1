class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.on_courses = []
        self.grades = {}

    def grade_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.on_courses and course in self.on_courses:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_value(self):
        sum_grades = 0
        count_grades = 0
        for value in self.grades.values():
            sum_grades += sum(value)
            count_grades += len(value)
        if count_grades == 0:
            print("Нет оценок")
        else:
            return sum_grades / count_grades

    def __str__(self):
        return f"Имя: {self.name} \nФамилия {self.surname}\n" \
               f"Средняя оценка за лекции {round(self.average_value(), 1)}\n" \
               f"Курсы в процессе изучения: {', '.join(self.on_courses)}\n" \
               f"Завершенные курсы {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_value() < other.average_value()
        else:
            print("Это не студент")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.on_courses = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def average_value(self):
        sum_grades = 0
        count_grades = 0
        for value in self.grades.values():
            sum_grades += sum(value)
            count_grades += len(value)
        if count_grades == 0:
            print('Нет оценок!')
        else:
            return sum_grades / count_grades

    def __str__(self):
        return f"Имя: {self.name} \nФамилия {self.surname}\n" \
               f"Средняя оценка за лекции {round(self.average_value(), 1)}"

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_value() < other.average_value()
        else:
            print("Это не лектор")


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.on_courses and course in student.on_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.on_courses += ['Python', 'Javascript']
student1.finished_courses += ["Введение в программирование"]

student2 = Student('Arseniy', 'Lebedev', 'man')
student2.on_courses += ['Python', 'Java']
student2.finished_courses += ["Git"]

lector1 = Lecturer('Alex', 'Frankson')
lector1.on_courses += ['Python', "Javascript"]

lector2 = Lecturer('Nina', 'Lisobina')
lector2.on_courses += ['Python', "Java"]

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.on_courses += ['Python']

cool_reviewer.rate_hw(student1, 'Python', 10)
cool_reviewer.rate_hw(student1, 'Python', 10)
cool_reviewer.rate_hw(student1, 'Python', 10)

cool_reviewer.rate_hw(student2, 'Python', 9)
cool_reviewer.rate_hw(student2, 'Python', 10)
cool_reviewer.rate_hw(student2, 'Python', 7)

student1.grade_lector(lector1, 'Python', 5)
student1.grade_lector(lector1, 'Python', 5)
student1.grade_lector(lector1, 'Python', 3)

student1.grade_lector(lector1, 'Javascript', 7)
student1.grade_lector(lector1, 'Javascript', 4)
student1.grade_lector(lector1, 'Javascript', 10)

student2.grade_lector(lector2, 'Python', 10)
student2.grade_lector(lector2, 'Python', 9)
student2.grade_lector(lector2, 'Python', 7)

student2.grade_lector(lector2, 'Java', 10)
student2.grade_lector(lector2, 'Java', 2)
student2.grade_lector(lector2, 'Java', 7)

# Создаем список студентов
student_list = [student1, student2]

# Создаем список лекторов
lecturer_list = [lector1, lector2]


def rating(list, course_name):
    sum_all = 0
    count_all = 0
    for person in list:
        if course_name in person.on_courses:
            sum_all += person.average_value()
            count_all += 1
    average_for_all = sum_all / count_all
    return round(average_for_all, 1)


print(student1.grades)
print(lector1.grades)
print(lector2.grades)
print(cool_reviewer)
print()
print(lector1)
print()
print(lector2)
print()
print(student1)
print()
print(student2)
print()
print("У первого лектора оценки хуже?", lector1 < lector2)
print()
print("У первого студента оценки хуже?", student1 < lector2)
print()
print(f"Средняя оценка для всех студентов по курсу {'Python'}: {rating(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {rating(lecturer_list, 'Python')}")
