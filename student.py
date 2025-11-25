import random

day_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
lectures = ['mathematics', 'geometry', 'computer science', 'foreign language', 'biology', 'geography', 'physics', 'physical education', 'music']
times = [9, 10, 11, 12, 13, 14]
names = ['Mark', 'Ivan', 'Kseniia', 'Max', 'Lena', 'Liza']

class Student():
    def __init__(self, name):
        self.name = name
        self.total = []

    def timetable(self):

        points = {'lessons' : 0}
        total_points = []

        for day in day_week:
            for time in times:
                lecture = random.choice(lectures)
                point = random.randint(5,100)
                total_points.append(point)
                points.update({lecture : point})
        self.total = total_points               
            
    def average_rating(self):
        
        ave_rating = sum(self.total) / len(self.total)
        return int(ave_rating)

class Grant(Student):
    def __init__(self, name):
        super().__init__(name)
        Student.timetable(self)
        Student.average_rating(self)

    def calculation_grant(self):
        a_r = Student.average_rating(self)
        dop_points = [-5, 5, 10]
        a_r = a_r + random.choice(dop_points)
        if random.random() < 0.55:
            a_r = a_r + 15
            print('+15')
        else:
            print('No benefits')    
        
        if a_r <= 60:
            grant = 500
        elif a_r <= 80:
            grant = 600    
        else:
            grant = 1000

        return 'Total points: ', a_r,'Grant size: ', grant        

for name in names:        
    students = [Grant(name)]
    for student in students:
        print(name,'-', student.calculation_grant())
        
    