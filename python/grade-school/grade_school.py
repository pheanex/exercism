class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.__school_grades = []
        for n in range(10):
            self.__school_grades.insert(n, [])

    def grade(self, grade_number):
        return self.__school_grades[grade_number]

    def add(self, studentname, grade):
        self.__school_grades[grade].append(studentname)
        self.__school_grades[grade] = sorted(self.__school_grades[grade])

    def sort(self):
        grade_list = []
        for grade, grade_nr in zip(self.__school_grades, range(10)):
            if len(grade):
                grade_list.append((grade_nr, tuple(grade)))
        return grade_list
