#OOPR-Assgn-20
#Start writing your code here
class Applicant:
    __application_dict={"A":4,"B":3,"C":5}
    __applicant_id_count=1000
    
    def __init__(self,applicant_name):
        self.__applicant_id=None
        self.__applicant_name=applicant_name
        self.__job_band=None
    @staticmethod
    def get_application_dict():
        return Applicant.__application_dict
        
    def get_applicant_name(self):
        return self.__applicant_name
    def get_applicant_id(self):
        return self.__applicant_id
    def get_job_band(self):
        return self.__job_band
        
    def generate_applicant_id(self):
        Applicant.__applicant_id_count+=1 
        self.__applicant_id=Applicant.__applicant_id_count
    
    def apply_for_job(self,job_band):
        if Applicant.__application_dict[job_band]<5:
            Applicant.__application_dict[job_band]+=1
            self.generate_applicant_id()
            self.__job_band=job_band
        else:
            return -1

a1=Applicant("Vetri")
if a1.apply_for_job("A") !=-1:
    print(a1.get_applicant_id(),a1.get_applicant_name(),a1.get_job_band())
else:
    print("Invalid Job band")
