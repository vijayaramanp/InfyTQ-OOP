#OOPR-Exer-1
                                                        
def purchase_mobile(price,brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    print("Total price of mobile is "+str(total_price))
    
def purchase_shoe(price,material):
    if material == "leather":
         total_price = price + price * 5 / 100
    else:
        total_price = price + price * 2 / 100
    print("Total price of shoe is "+str(total_price))
    

purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")

