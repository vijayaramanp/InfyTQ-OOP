#OOPR-Assgn-22
class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=[None,None]
    __list_ticket_price=[150,200]
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers
    def book_ticket(self, movie_name, number_of_tickets):
        if movie_name in Multiplex.__list_movie_name:
            movie_index=Multiplex.__list_movie_name.index(movie_name)
            if self.check_seat_availability(movie_index,number_of_tickets):
                tmp_lst=self.generate_seat_number(movie_index,number_of_tickets)
                self.__seat_numbers=tmp_lst
                self.calculate_ticket_price(movie_index,number_of_tickets)
            else:
                return -1
        else:
            return 0
                
    def  generate_seat_number(self,movie_index, number_of_tickets):
        seat_list=[]
        if Multiplex.__list_movie_name[movie_index]=="movie1":
            if Multiplex.__list_last_seat_number[0] != None:
                tmp=Multiplex.__list_last_seat_number[0].split('-')
                last_seat=int(tmp[1])
            else:
                last_seat=0 
            for i in range(1,number_of_tickets+1):
                last_seat+=1 
                seat_number="M1-"+str(last_seat)
                seat_list.append(seat_number)
            Multiplex.__list_last_seat_number[0]=seat_number
            Multiplex.__list_total_tickets[0] -= number_of_tickets
            return seat_list
            
                
        elif Multiplex.__list_movie_name[movie_index]=="movie2":
            if Multiplex.__list_last_seat_number[1] != None:
                tmp=Multiplex.__list_last_seat_number[1].split('-')
                last_seat=int(tmp[1])
            else:
                last_seat=0 
            for i in range(1,number_of_tickets+1):
                last_seat+=1 
                seat_number="M2-"+str(last_seat)
                seat_list.append(seat_number)
            Multiplex.__list_last_seat_number[1]=seat_number
            Multiplex.__list_total_tickets[1] -= number_of_tickets
            return seat_list
            
                
booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie2",6)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())
