#OOPR-Assgn-13
#Start writing your code here
class Classroom:
    classroom_list=["L135","II"]
    
    @staticmethod
    def search_classroom(class_room):
        for cls in Classroom.classroom_list:
            if cls.lower()==class_room.lower():
                return "Found"
            else:
                return -1 
                
print(Classroom.search_classroom("l135"))
