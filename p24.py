class Student:

    def __init__(self):
        self.name = input("Enter your name: ")

        self.marks = []
        self.total = 0

        for i in range(1, 4):
            mark = int(input("Enter marks of subject {}: ".format(i)))
            self.marks.append(mark)
            self.total += mark

    def average(self):
        self.average_score = self.total / 3
        print("Name :", self.name)
        print("Marks :", self.marks)
        print("Total :", self.total)
        print("Average :", self.average_score)


s1 = Student()

s1.average()