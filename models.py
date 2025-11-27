from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
base = declarative_base()

class Student(base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    
    # Relationship to Course
    courses = relationship("Course", back_populates="student")
    
class Course(base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='CASCADE'))
    
    # Relationship to Student
    student = relationship("Student", back_populates="courses")

if __name__ == "__main__":
    engine = create_engine('sqlite:///moringa.db')
    base.metadata.create_all(engine)