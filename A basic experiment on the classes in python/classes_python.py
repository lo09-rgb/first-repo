class Student:
    def __init__(self, rollno, name, m1, m2, m3, m4, m5):
        self.RollNo = rollno
        self.Name = name
        self.M1 = m1
        self.M2 = m2
        self.M3 = m3
        self.M4 = m4
        self.M5 = m5
        self.Total = 0
        self.Average = 0
        self.Grade = ""

    def Calculate_Total(self):
        self.Total = self.M1 + self.M2 + self.M3 + self.M4 + self.M5

    def Calculate_Average(self):
        self.Average = self.Total / 5

    def Find_Grade(self):
        if self.Average > 90 and self.Average <= 100:
            self.Grade = "A"
        elif self.Average > 80 and self.Average <= 90:
            self.Grade = "B"
        elif self.Average > 70 and self.Average <= 80:
            self.Grade = "C"
        elif self.Average > 60 and self.Average <= 70:
            self.Grade = "D+"
        else:
            self.Grade = "F"

    def Display(self):
        print("Roll No :" , self.RollNo)
        print("Name     :" , self.Name)
        print("Total    :" , self.Total)
        print("Average  :" , self.Average)
        print("Grade    :" , self.Grade)



roll = int(input("Enter Roll No: "))
name = input("Enter Name: ")

m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))
m4 = int(input("Enter Marks 4: "))
m5 = int(input("Enter Marks 5: "))

s = Student(roll, name, m1, m2, m3, m4, m5)

s.Calculate_Total()
s.Calculate_Average()
s.Find_Grade()

print("\nStudent Details")
s.Display()
#__rollno this 2 underscore tell us that our variable is private
    
