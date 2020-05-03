#OOPR-Assgn-27
#This class represents ThemePark
class ThemePark:
    #dict_of_games contains the game name as key, price/ride and points that can be earned by customer in a list as value
    dict_of_games={"Game1":[35.5,5], "Game2":[40.0,6],"Game3":[120.0,10], "Game4":[60.0,7],"Game5":[25.0,4]}
    @staticmethod
    def validate_game(game_input):
        if game_input in ThemePark.dict_of_games:
            return True
        else:
            return False
        #If game_input is present in ThemePark, return true. Else, return false.
    @staticmethod
    def get_points(game_input):
        return ThemePark.dict_of_games[game_input][1]
        #Return the points that can be earned for the given game_input.
    @staticmethod
    def get_amount(game_input):
        return ThemePark.dict_of_games[game_input][0]
        #Return the price/ride for the given game_input
#print(ThemePark.validate_game("Game2"))
#This class represents ticket
class Ticket:
    __ticket_count=200
    def __init__(self):
        self.__ticket_id=None
        self.__ticket_amount=0
    def generate_ticket_id(self):
        Ticket.__ticket_count+=1
        self.__ticket_id=Ticket.__ticket_count
        #Auto-generate ticket_id starting from 201
    def calculate_amount(self, list_of_games):
        flag=0
        tmp=0
        for game in list_of_games:
            if ThemePark.validate_game(game):
                tmp=tmp+ThemePark.get_amount(game)
            else:
                flag=1 
                break
        if flag==0:
            self.__ticket_amount=tmp 
            return True 
        else:
            return False
        '''Validate the games in the list_of_games.
        If all games are valid, calculate total ticket amount and assign it to attribute, ticket_amount and return true. Else, return false'''
    def get_ticket_id(self):
        return self.__ticket_id
    def get_ticket_amount(self):
        return self.__ticket_amount

class Customer:
    def __init__(self,name,list_of_games):
        self.__name=name
        self.__list_of_games=list_of_games
        self.__ticket=0
        self.__points_earned=0
        self.__food_coupon="No"
        
    def play_game(self):
        total_points=0
        if "Game3" in self.__list_of_games and "Game2" not in self.__list_of_games:
            self.__list_of_games.append("Game2")
        for game in self.__list_of_games:
            total_points+=ThemePark.get_points(game)
        self.__points_earned=total_points
        
    def update_food_coupon(self):
        if "Game4" in self.__list_of_games and self.__points_earned > 15:
            self.__food_coupon="Yes"
            
    def book_ticket(self):
        t1=Ticket()
        if t1.calculate_amount(self.__list_of_games):
            t1.generate_ticket_id()
            self.play_game()
            self.update_food_coupon()
            
            return True 
        else:
            return False 
            
    def get_name(self):
        return self.__name
    def get_list_of_games(self):
        return self.__list_of_games
    def get_ticket(self):
        return self.__ticket
    def get_points_earned(self):
        return self.__points_earned
    def get_food_coupon(self):
        return self.__food_coupon

        
cust1=Customer("Vetri",["Game1","Game2"])
if cust1.book_ticket():
    print(cust1.get_name(),cust1.get_list_of_games(),cust1.get_ticket(),cust1.get_points_earned(),cust1.get_food_coupon())
'''Represent customers and display all details of the customer, if he is able to book the ticket and play the game. Else, display appropriate error message '''
