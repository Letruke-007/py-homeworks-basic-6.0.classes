class Student:
    def __init__(self, name: object, surname: object, gender: object) -> object:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer: object, course: object, grade: object) -> object:
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_num(self):
        counter_sum_grades = 0
        counter_num_grades = 0
        for key, val in self.grades.items():
            for i in val:
                counter_sum_grades += i
                counter_num_grades += 1
        avg_number = counter_sum_grades / counter_num_grades
        return avg_number

    def __cmp__(self, other):
        if self.avg_num() > other.avg_num():
            return (f'Средняя оценка студента {self.name} {self.surname} равна {self.avg_num()}, что больше, '
                    f'чем средняя оценка студента {other.name} {other.surname}, равная {other.avg_num()}')
        elif self.avg_num() < other.avg_num():
            return (f'Средняя оценка студента {self.name} {self.surname} равна {self.avg_num()}, что меньше, '
                    f'чем средняя оценка студента {other.name} {other.surname}, равная {other.avg_num()}')
        elif self.avg_num() == other.avg_num():
            return (f'Средняя оценка студента {self.name} {self.surname} равна средней оценке студента {other.name} '
                    f'{other.surname} и составляет {other.avg_num()}')

    def __str__(self):
        return(f'Имя: {self.name}'
               f'\nФамилия: {self.surname}'
               f'\nСредняя оценка за домашние задания: {self.avg_num()}'
               f'\nКурсы в процессе изучения: '
               f'{", ".join(self.courses_in_progress)}'
               f'\nЗавершенные курсы: '
               f'{", ".join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = courses_attached


class Lecturer(Mentor):
    def __init__(self, name: object, surname: object, courses_attached) -> object:
        super().__init__(name, surname, courses_attached)
        self.grades = {}

    def avg_num(self):
        counter_sum_grades = 0
        counter_num_grades = 0
        for key, val in self.grades.items():
            for i in val:
                counter_sum_grades += i
                counter_num_grades += 1
        avg_number = counter_sum_grades / counter_num_grades
        return avg_number

    def __cmp__(self, other):
        if self.avg_num() > other.avg_num():
            return (f'Средняя оценка лектора {self.name} {self.surname} равна {self.avg_num()}, что больше, '
                f'чем средняя оценка лектора {other.name} {other.surname}, равная {other.avg_num()}')
        elif self.avg_num() < other.avg_num():
            return (f'Средняя оценка лектора {self.name} {self.surname} равна {self.avg_num()}, что меньше, '
                f'чем средняя оценка лектора {other.name} {other.surname}, равная {other.avg_num()}')
        elif self.avg_num() == other.avg_num():
            return (f'Средняя оценка лектора {self.name} {self.surname} равна средней оценке лектора {other.name} '
                    f'{other.surname} и составляет {other.avg_num()}')

    def __str__(self):
        return(f'Имя: {self.name}'
               f'\nФамилия: {self.surname}'
               f'\nСредняя оценка за лекции: {self.avg_num()}')


class Reviewer(Mentor):
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname, courses_attached)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return(f'Имя: {self.name}'
               f'\nФамилия: {self.surname}')


def avg_grade_students_course(students, course_name):
    counter_sum_grades = 0
    counter_num_grades = 0
    for student in students:
        if isinstance(student, Student):
            for key, val in student.grades.items():
                if key == course_name:
                    for i in val:
                        counter_sum_grades += i
                        counter_num_grades += 1
    if counter_num_grades == 0:
        return 'Оценки не найдены'
    else:
        avg_gr_st_cr = counter_sum_grades / counter_num_grades
        return (f'Средняя оценка студентов за домашние работы на курсе {course_name} '
                f'составляет {avg_gr_st_cr} баллов из 10')

def avg_grade_lecturers_course(lecturers, course_name):
    counter_sum_grades = 0
    counter_num_grades = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            for key, val in lecturer.grades.items():
                if key == course_name:
                    for i in val:
                        counter_sum_grades += i
                        counter_num_grades += 1
    if counter_num_grades == 0:
        return 'Оценки не найдены'
    else:
        avg_gr_st_cr = counter_sum_grades / counter_num_grades
        return (f'Средняя оценка лекторов за лекции на курсе {course_name} '
                f'составляет {avg_gr_st_cr} баллов из 10')

clever_student = Student('Ruoy', 'Eman', 'male')
stupid_student = Student('Joe', 'Biden', 'male')

students = [stupid_student, clever_student]

clever_student.courses_in_progress += ['Python']
clever_student.courses_in_progress += ['Java']
clever_student.finished_courses += ['Oracle']

stupid_student.courses_in_progress += ['Python']
stupid_student.courses_in_progress += ['Java']

good_lecturer = Lecturer('Good', 'Buddy', 'Python')
bad_lecturer: Lecturer = Lecturer('Bad', 'Guy', 'Python')

lecturers = [good_lecturer, bad_lecturer]

reviewer1 = Reviewer('John', 'Snow', 'Python')
reviewer2 = Reviewer('Alex', 'Johnson', 'Python')

reviewer1.rate_hw(clever_student, 'Python', 10)
reviewer1.rate_hw(stupid_student, 'Python', 5)

reviewer2.rate_hw(clever_student, 'Python', 9)
reviewer2.rate_hw(stupid_student, 'Python', 4)

clever_student.rate_lecturer(good_lecturer,'Python', 10)
clever_student.rate_lecturer(good_lecturer,'Python', 8)
clever_student.rate_lecturer(bad_lecturer,'Python', 5)
clever_student.rate_lecturer(bad_lecturer,'Python', 6)

stupid_student.rate_lecturer(good_lecturer, 'Python', 9)
stupid_student.rate_lecturer(good_lecturer, 'Python', 9)
stupid_student.rate_lecturer(bad_lecturer, 'Python', 8)
stupid_student.rate_lecturer(bad_lecturer, 'Python', 8)

print('Список студентов:')
print(clever_student)
print(stupid_student)
print()
print('Список лекторов:')
print(good_lecturer)
print(bad_lecturer)
print()
print('Список экспертов:')
print(reviewer1)
print(reviewer2)
print()

print(clever_student.__cmp__(stupid_student))
print(stupid_student.__cmp__(clever_student))
print(clever_student.__cmp__(clever_student))

print(good_lecturer.__cmp__(bad_lecturer))
print(bad_lecturer.__cmp__(good_lecturer))
print(good_lecturer.__cmp__(good_lecturer))

print(avg_grade_students_course(students, 'Java'))
print(avg_grade_lecturers_course(lecturers, 'Python'))
