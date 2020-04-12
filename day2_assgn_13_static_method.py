#OOPR-Assgn-13
#Start writing your code here
class Classroom:
    classroom_list=["L135","II"]
    
    @staticmethod
    def search_classroom(class_room):
        if class_room.upper() in Classroom.classroom_list:
            return "Found"
        else:
            return -1 
                
if Classroom.search_classroom("l135")=="Found":
    print("Classroom Found")
else:
    print("Classroom not Found")
