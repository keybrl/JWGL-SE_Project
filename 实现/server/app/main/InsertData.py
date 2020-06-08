from ..models import *
from .. import app, db
import csv
import os
import pandas as pd

data_dir = 'D:\Code\SE-Project\data'


def get_data():
    filelist = os.listdir(data_dir)
    file_data = {}
    for file in filelist:
        print(file)
        with open(os.path.join(data_dir, file)) as csv_file:
            reader = csv.DictReader(csv_file)
            all_data = [data for data in reader]
            file_data[file[:-4]] = all_data
    return file_data


def insert_into_account(data_list):
    for data in data_list:
        acc = Account(account=data['account'], password=data['passwd'], type=data['type'])
        if acc.type == 'root':
            app.config['FLASKY_ADMIN'].append(acc.account)
        db.session.add(acc)
    db.session.commit()


def insert_into_student(data_list):
    for data in data_list:
        stu = Student(id=data['id'], name=data['name'],
                      year=data['year'])
        db.session.add(stu)
    db.session.commit()


def insert_into_instructor(data_list):
    for data in data_list:
        ins = Instructor(id=data['id'], name=data['name'])
        db.session.add(ins)
    db.session.commit()


def insert_into_superior(data_list):
    for data in data_list:
        sup = Superior(id=data['id'],name=data['name'])
        db.session.add(sup)
    db.session.commit()


def insert_into_admin(data_list):
    for data in data_list:
        adm = Admin(id=data['id'], name=data['name'])
        db.session.add(adm)
    db.session.commit()


def insert_into_course(data_list):
    for data in data_list:
        course = Course(id=data['id'], name=data['name'], type=data['type'],
                        credit=data['credit'], period=data['period'])
        db.session.add(course)
    db.session.commit()


def insert_into_classroom(data_list):
    for data in data_list:
        classroom = Classroom(id=data['id'], building=data['building'],floor=data['floor'],
                              number=data['number'])
        db.session.add(classroom)
    db.session.commit()


def insert_into_class(data_list):
    for data in data_list:
        cla = Class(id=data['id'],year=data['year'],term=data['term'], number=data['number'],
                    max_people=data['max_people'],optional=bool(int(data['optional'])))
        course = Course.query.filter_by(id=data['course_id']).first()
        if course is not None:
            cla.course = course
            db.session.add(cla)
    db.session.commit()


def insert_into_exam(data_list):
    for data in data_list:
        exam = Exam(id=data['id'], date=data['date'], time=data['time'])
        cla = Class.query.filter_by(id =data['class_id']).first()
        if cla is not None:
            exam.classes = cla
            db.session.add(exam)
    db.session.commit()


def insert_into_Curricula_variable(data_list):
    for data in data_list:
        stu = Student.query.filter_by(id=data['student_id']).first()
        cla = Class.query.filter_by(id=data['class_id']).first()
        grade = data.get('grade')
        if stu is not None and cla is not None:
            if grade is None:
                grade = 0
            c_v = CurriculaVariable(student=stu,classes=cla,grade=grade)
            db.session.add(c_v)
    db.session.commit()


def insert_into_Teach(data_list):
    for data in data_list:
        ins = Instructor.query.filter_by(id=data['instructor_id']).first()
        cla = Class.query.filter_by(id=data['class_id']).first()
        if ins is not None and cla is not None:
            teach = Teach(teacher=ins,classes=cla)
            db.session.add(teach)
    db.session.commit()


def insert_into_Schedule(data_list):
    for data in data_list:
        cla = Class.query.filter_by(id=data['class_id']).first()
        classroom = Classroom.query.filter_by(id=data['classroom_id']).first()
        if cla is not None and classroom is not None:
            sch = Schedule(classes=cla,classroom=classroom,week=data['week'],
                           day=data['day'],section=data['section'])
            db.session.add(sch)
        db.session.commit()


def insert_into_Exam_room(data_list):
    print(data_list)
    for data in data_list:
        exam = Exam.query.filter_by(id=data['exam_id']).first()
        classroom = Classroom.query.filter_by(id=data['classroom_id']).first()
        print(exam.id, classroom.id)
        if exam is not None and classroom is not None:
            E_R = Exam_room(exam=exam,classroom=classroom)
            db.session.add(E_R)
    db.session.commit()


def insert_into_Take_exam(data_list):
    for data in data_list:
        exam = Exam.query.filter_by(id=data['exam_id']).first()
        student = Student.query.filter_by(id=data['student_id']).first()
        exam_grade= data.get('exam_grade')
        if exam is not None and student is not None:
            if exam_grade is None:
                exam_grade = 0
            T_E = Take_exam(student=student,exam=exam,exam_grade=exam_grade)
            db.session.add(T_E)
    db.session.commit()


insert_list = {'account': insert_into_account,
               'student': insert_into_student,
               'instructor': insert_into_instructor,
               'superior': insert_into_superior,
               'admin': insert_into_admin,
               'course': insert_into_course,
               'classroom': insert_into_classroom,
               'class': insert_into_class,
               'exam': insert_into_exam,
                'curricula_variable':insert_into_Curricula_variable,
                'teach':insert_into_Teach,
                'schedule':insert_into_Schedule,
                'exam_room':insert_into_Exam_room,
                'take_the_exam':insert_into_Take_exam,
                'teach':insert_into_Teach}


def main():
    file_data = get_data()
    for fun in insert_list:
        insert_list[fun](file_data[fun])


def change_to_csv(data_file):
    os.chdir(data_dir)
    data_xlsx = pd.read_excel(data_file+'.xlsx', index_col=0)
    return data_xlsx


def fake_data_classroom():
    for block in ['A', 'B', 'C', 'D', 'E']:
        for floor in range(1, 6):
            for number in range(1, 26):
                id = block+'-'+str(floor)+str(number)
                if number < 10:
                    id = block + '-' + str(floor) + '0' + str(number)
                classroom = Classroom(id=id, building=block, floor=floor, number=number)
                db.session.add(classroom)
                try:
                    db.session.commit()
                except:
                    db.session.rollback()
