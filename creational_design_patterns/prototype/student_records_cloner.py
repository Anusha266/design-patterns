
import copy
class Student():
    def __init__(self,builder):
        self.name = builder.name
        self.cls = builder.cls 
        self.grade = builder.grade 
    
    def display(self):
        print(f"Name={self.name}--class:{self.cls}--grade:{self.grade}")
    
    def clone(self):
        return copy.deepcopy(self)
    
class StudentBuilder():
    def __init__(self):
        self.name='Anusha'
        self.cls = 'C4'
        self.grade = 'A+' 
    def set_name(self,name):
        self.name=name
        return self
    def set_cls(self,cls):
        self.cls=cls
        return self
    def set_grade(self,grade):
        self.grade = grade 
        return self
    def build(self):
        return Student(self)


if __name__=='__main__':
    base_student = StudentBuilder().set_name("xyz").set_cls("c5").set_grade("B").build()
    base_student.display()
    
    student_1 = base_student.clone()
    student_1.name="venu"
    student_1.display()
    
    
'''
Prototype is often combined with Builder because Builder simplifies initial construction of a complex object, while Prototype simplifies subsequent duplication.

Builder = first clean creation.

Prototype = efficient cloning.
Together, they reduce both constructor complexity and duplication overhead.

'''