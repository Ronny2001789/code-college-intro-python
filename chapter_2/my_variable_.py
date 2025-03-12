# name = "ronny"

# surname = "mputla"

# print(name + surname)

# my_sentence = "the new world"

# print(my_sentence.title())


# my_initial = f"{name} {surname}"

# print(my_initial)


# my_name = "moronza"
 
# my_players= "dybala"

# my_car = "bmw"
 
# full_data = f"{my_name} {my_players} {my_car}"


# print(full_data)

# rules = "please attend everyday "
 
# print("\tmr david said " + rules  ) 

# print("good things take time.\nall people deserve the best.\n\tteachers always have time for students ")



# my_name,surname,my_car ="ronny","mputla","bmw"
# print(my_name + my_car)

# nostarch_url = 'https://nostarch.com'
# nostarch_url.removeprefix('https://')

# 3 + 5

class House:

    def __init__(self,motho,koloi,meetse):
        self.motho = motho
        self.koloi = koloi
        self.meetse = meetse

    def my_petrol(self):
        print(f"This is my name {self.motho} and these is my car {self.koloi} ")


    def The_router (self):
        print(f"The new world is around the gorner {self.motho} and {self.meetse})")

   

    def motho_ke (self):
        cow = input("enter your name")
        if cow == "Ronny" :
            print( f"The human being the always have something to dod with in life like {self.koloi} le {self.motho}")
            print("mputla ronny")

full_name = House("ronny","bmw",2)
full_name.my_petrol()
full_name.The_router()
full_name.motho_ke()





