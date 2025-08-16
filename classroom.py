class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

def calculate_averages(students_dict):
    students = [Student(name, marks) for name, marks in students_dict.items()]
    averages = {student.name: round(student.average(), 2) for student in students}
    top_performer = max(students, key=lambda s: s.average()).name
    return averages, top_performer

# Input example
students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages, top_performer = calculate_averages(students)

print("Average Marks:", averages)
print("Top Performer:", top_performer)
