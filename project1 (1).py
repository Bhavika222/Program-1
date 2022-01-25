#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Restaurant:
    def_init_(self):
        self.food = {}  #(1:"Tandoori Chicken")5 food items
        self.food_id = len(self.food)+1
        self.ordered_item =[]
        self.personal_details={}
#Admin functionolities
    def food_items(self):
        self.name = input("Enter the food name")
        self.quantity = int(input("Enter the quantity : kg"))
        self.price = float(input("Enter the price: "))
        self stock =int(input("Enter the stock in kg"))
        self.discount = int(input("Enter discount value"))
        self.item = {"name":self.name , "price":self.price,"discount":self.discount,"stock":self.stock}
        self.food_id = len(self.food)+1
        self.foods[self.food_id] = self.item  
        print("Item added Sucessfully \n", self.food)
    
    def remove_items(self):
        del self.food[int(input("Enter the food id you want to delete:"))]
        print("Item is deleted Succesfully")
        print("Remaining food items are " , self.food)
    
    
    def edit_food_items(self):
        f_id = int(input("Enter the food id you want to update:"))
        #{1:Tandoori Chicken,2:Vegan Burger ,3:Truffle Cake""}
        for i in self.food[f_id]:
            self.food[f_id] = input(f" Enter the"+i+ "you want to update:")
        print("Food items is updated succesfully\n",self.food)
        
    def all_food_items(self):
        printt("List of all food items are:")
        for i in self.food:
            print("Food id :",i,"\n")
            for j in self.food[i]:
                print(j,":",self.food[i][j])
                
                
                
#user functionalities
     def register(self):
        self.fullname = input("Enter Your Full Name")
        self.phone_number = int(input("Enter 10 Digit Mobile Number"))
        self.email = input("Enter Your Email")
        self.address = input("Enter your Full Adress")
        self.username = input("choose Your User Name")
        self.password = input("choose your Password")
        self.confirm_password = input("Confirm Your Password")
        self.personal_details = {"fullname":self.fullname , "phonenumber":self.phone_number , "email":self.email , "address":self.address}
        
        if password != confirm_password:
            print("password Don't Match !!!")
            
        else:
            if len(password) <= 6:
                print("Password Is Too Short......Please Chosse Strong Password")
                
            else:
                print("Congratulation......!!! Your Account Created Successfully")
                                 
        def login(self):
            while True:
                user_id = input("Enter your userid")
                password = input("Enter your password")
                if user_id == self.username:
                    if password == self.password:
                        print("Congratulation youbhave sucessfully login")
                        break
                        else:
                            print("Incorrect details")
                            
                def place_food_item(self):
                    list_of_foodite = {} #put all food items
                    print("Menu list") #1,2,3
                    user_input = int(input("Select food item you need to place"))
                    if user_input==1:
                        self.ordered_item.append()
                    if user_input==2:  
                        
                    else:
                        print("choose form the Menu")
                        
                    def order_history(self):
                        for i in ordered_item:
                            print(i)
                        
                    
                
    

