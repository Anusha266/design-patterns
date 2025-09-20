'''
Resume Builder  (Requirements):

Resume should support multiple sections:

PersonalInfo (mandatory)

Education (optional, multiple entries)

Experience (optional, multiple entries)


The ResumeBuilder should provide methods to add each section step by step.

Example: .add_education("B.Tech, CSE, XYZ University")

Example: .add_skill("Python")

Once built, the Resume object should support a .display() method to print all the details.

The system should allow different resume formats:

SimpleResumeBuilder (basic text resume)

DetailedResumeBuilder (includes projects, certifications, etc.)

Extensibility: Adding a new section (e.g., Languages) should only require extending the builder, not modifying the core Resume class.
'''


class Resume():
    def __init__(self,builder):
        self.name = builder.name
        self.education = builder.education
        self.experience = builder.experience
        self.projects = builder.projects
         
    def display(self):
        print(f"name={self.name},education={self.education},experience = {self.experience},projects={self.projects}")
        
class ResumeBuilder():
    def __init__(self):
        self.name=None
        self.education=None
        self.experience=None
        self.projects=[]
        
    def set_name(self,name):
        self.name=name
        return self
    def set_education(self,education):
        self.education = education
        return self
    def set_experience(self,experience):
        self.experience=experience
        return self
    def set_project(self,project):
        self.projects.append(project)
        return self
    def build(self):
        return Resume(self)
    
         
class ResumeDirector():

    def simpleResumeBuilder(self):
        return ResumeBuilder().set_name("Anusha").set_experience("1 year").build()
    
    def detailedResumeBuilder(self):
        return ResumeBuilder().set_name("venu").set_education("NBKR").set_experience("4 years").set_project("Todo list app").set_project("Life Builder").build()
    
#client code

if __name__=='__main__':
    resume_director = ResumeDirector()
    resume_director.simpleResumeBuilder().display()
    resume_director.detailedResumeBuilder().display()
    
    
    
'''
Resume Builder can built using prototype pattern too..because cloning all details and changing enough ones would be easier

'''