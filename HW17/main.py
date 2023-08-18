from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = "postgresql://{user}:{password}@{host}:{port}/{database}"


engine = create_engine(
    DATABASE_URI.format(
        host="localhost",
        database="projector",
        user="ananasia",
        password="password",
        port=5432,
    )
)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __str__(self):
        return f"This is {self.id} student {self.name}. Age: {self.age}"

    def __repr__(self):
        return f"This is {self.id} student {self.name}. Age: {self.age}"


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    students_amount = Column(Integer)


class Student_subject(Base):
    __tablename__ = "student_subject"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    subject_id = Column(Integer, ForeignKey("subject.id"))


Base.metadata.create_all(engine)

session = Session()

english_students = (
    session.query(Student)
    .join(Student_subject, Student.id == Student_subject.student_id)
    .join(Subject, Student_subject.subject_id == Subject.id)
    .filter(Subject.name == "English")
    .all()
)

for student in english_students:
    print(student.name)

session.close()

new_student = Student(name="Jerry", age=25)
session.add(new_student)
session.commit()
all_students = session.query(Student).all()
for student in all_students:
    print(student)
