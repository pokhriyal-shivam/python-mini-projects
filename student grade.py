class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

try:
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    s1 = Student(name, marks)

    with open("result.txt", "a") as f:
        f.write(f"{s1.name} - {s1.marks} - {s1.grade()}\n")

    print("Saved Successfully")

except ValueError:
    print("Marks must be number")
