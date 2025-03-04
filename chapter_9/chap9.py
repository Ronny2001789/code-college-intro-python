# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting.")

#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

#Creating three different instances of Restaurant
restaurant1 = Restaurant("The Gourmet Bistro", "French")
restaurant2 = Restaurant("Sushi Paradise", "Japanese")
restaurant3 = Restaurant("Pasta Heaven", "Italian")

##Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, location):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location

    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

##Creating several instances of User
user1 = User("Ethan", "Hurwitz", "Joburg")
user2 = User("Ronny", "Mputla", "Los Angeles")
user3 = User("Pierre", "Kahunda", "Chicago")

##Calling both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()




class my_family:

        def __init__(self,mable,jim,race):
            self.mable = mable
            self.jim = jim
            self.race = race

        def my_information_name(self):
            my_list = f"{self.race} {self.jim} {self.mable}"
            return my_list.upper() 
        
my_province_motho =("lesea","media","laptop")
print(my_province_motho.my_information_name())








