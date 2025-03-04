## class_1
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def  my_personality(self):
#         return f"Hello, my name is {self.name}!"

#     def my_teammates(self):
#         self.age += 1
#         return f"Happy Birthday! You are now {self.age} years old."


# person1 = Person("Alice", 25)
# print(person1.my_personality())  
# print(person1.my_teammates())  

## class_2
# class Person:
#     def __init__(self, name, age, team):  #
#         self.name = name
#         self.age = age
#         self.team = team

#     def greet(self):
#         return f"Hello, {self.name} here! Nice to meet you ✌🏽!"

#     def how_old_are_you(self):
#         return f"WOW, you're old! You're {self.age} years old."

#     def team_name(self, new_team):
#         old_team = self.team
#         self.team = new_team
#         return f"{self.name} has switched from {old_team} to {new_team}."

# ##Example usage
# person1 = Person("Pierre", 218, "404 Avengers")

# print(person1.greet())
# print(person1.how_old_are_you())
# print(person1.team_name("Stack overflow"))
# print(person1.team_name("Function Junction"))
# print(f"Current Team: {person1.team}")

## class_3
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

## Creating three different instances of Restaurant
restaurant1 = Restaurant("The Gourmet Bistro", "French")
restaurant2 = Restaurant("Sushi Paradise", "Japanese")
restaurant3 = Restaurant("Pasta Heaven", "Italian")

## Calling describe_restaurant() for each instance
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





