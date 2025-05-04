class student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.rollno)


zulkar = student("Zulkarnain", 20, 12345)
zulkar.display()