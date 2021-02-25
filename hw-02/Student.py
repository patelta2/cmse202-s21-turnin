# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, year=0):
        self.name = name
        self.gpa = gpa
        self.year = year
        
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        
    def enroll(self,courses):
        '''
        takes as input a list of courses and 
        adds them as an attribute to the student
        '''
        self.courses = courses
        
    def display_courses(self):
        '''
        prints out courses
        '''
        print("I am enrolled in:", self.courses)
        
    def years_until_graduation(self):
        '''
        returns remaining years till graduating.
        '''
        return 4-self.year
        

class Spartan():
    def __init__(self, name = ""):
        self.name = name
        
        
    def set_motto(self,motto):
        '''
        Set the motto
        '''
        self.motto = motto
        
    def get_name(self):
        '''
        Print name
        '''
        print("My name is", self.name)
        
        
    def school_spirit(self):
        '''
        Print motto statement
        '''
        print("I am a Spartan. My motto is",self.motto)
        
       
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        