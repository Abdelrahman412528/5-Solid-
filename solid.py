class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"

class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __str__(self):
        return f"Subject: {self.name} (Code: {self.code})"


class Formatter:
    def format(self, items):
        raise NotImplementedError("Subclasses should implement this method!")

class SimpleFormatter(Formatter):
    def format(self, items):
        return "\n".join(str(item) for item in items)

class JSONFormatter(Formatter):
    def format(self, items):
        import json
        return json.dumps([item.__dict__ for item in items], indent=2)

class OnlineStudent(Student):
    def __init__(self, name, student_id, email):
        super().__init__(name, student_id)
        self.email = email
    def __str__(self):
        return f"Online Student: {self.name} (ID: {self.student_id}, Email: {self.email})"

class Addable:
    def add(self, item):
        raise NotImplementedError("Subclasses should implement this method!")


class Removable:
    def remove(self, item):
        raise NotImplementedError("Subclasses should implement this method!")


class StudentManager(Addable, Removable):
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def remove(self, student):
        self.students.remove(student)

    def get_all(self):
        return self.students

class UniversitySystem:
    def __init__(self, manager, formatter):
        self.manager = manager
        self.formatter = formatter

    def add_student(self, student):
        self.manager.add(student)

    def display_students(self):
        students = self.manager.get_all()
        return self.formatter.format(students)



def main():
    manager = StudentManager()
    formatter = SimpleFormatter() 
    system = UniversitySystem(manager, formatter)

    student1 = Student("Ahmed", 20230122)
    student2 = OnlineStudent("Abdelrahman", 20230123, "abdo@gmail.com")

    system.add_student(student1)
    system.add_student(student2)

    print("All Students:")
    print(system.display_students())


if __name__ == "__main__":
    main()
