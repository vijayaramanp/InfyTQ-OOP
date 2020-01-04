#OOPR-Assgn-7
#Start writing your code here
class Instructor:
    def __init__(self):
        self.__instructor_name=None 
        self.__technology_skill=[]
        self.__experience=None
        self.__avg_feedback=None
    def set_instructor_name(self,name):
        self.__instructor_name=name
    def get_instructor_name(self):
        return self.__instructor_name
        
    def set_technology_skill(self,lis):
        self.__technology_skill=lis 
    def get_technology_skill(self):
        return self.__technology_skill
    
    def  set_avg_feedback(self,avg):
        self.__avg_feedback=avg 
    def get_avg_feedback(self):
        return self.__avg_feedback
    
    def set_experience(self,exp):
        self.__experience=exp 
    def get_experience(self):
        return self.__experience
        
    
    def check_eligibility(self):
        pass
    def allocate_course(technology):
        pass
