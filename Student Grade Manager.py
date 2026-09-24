class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    def display(self):
        print(f"Student Name: {self.name} and Marks: {self.marks}")


def main():
    count = int(input("How many syudents?: "))
    students = []


    for _ in range(count):
        name = input("student name:")
        marks = input("student marks:")


        student = Student(name, marks)
        students.append(student)

    for student in students:
        student.display()

if __name__ == "__main__":
    main()