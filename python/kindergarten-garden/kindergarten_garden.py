class Garden:
    def __init__(self, spots, cups=4, students=None):
        self.rows = spots.split()
        self.cups = cups
        self.pots_in_row = self.cups // len(self.rows)
        if students is None:
            students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
                        "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
        students.sort()
        self.students = students
        self.plant_index = {"G": "Grass",
                            "C": "Clover",
                            "V": "Violets",
                            "R": "Radishes"}

    def plants(self, studentname):
        student = dict()
        student["name"] = studentname
        student["index"] = self.pots_in_row * self.students.index(studentname)
        student["plants"] = []
        for row in self.rows:
            student["plants"] += row[student["index"]:student["index"] + self.pots_in_row]
        return [self.plant_index[P] for P in student["plants"]]
