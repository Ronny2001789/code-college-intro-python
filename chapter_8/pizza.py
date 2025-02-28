def pizza_oven(*toppings):
    print(f"here is your {','.join(toppings)} pizza.")
    print("toppings")
    for topping in toppings:
        print(f"- {topping}")

pizza_oven("ham","cheese","pepper")
## single istrik allow key
def test(*first, second):
    print(f"these are my first arguments: {first}")
    print(f"this aisre my other argument: {second}")

test(1, 2, 3, 4, second = 5)
## double istrik = allow key and value
# def build_profile(first, last, **user_info):

#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

# print(user_profile)

# def my_cow(age,ace, **my_people):

#     kilometer_dope["name"] = age
#     kilometers_dope["house"] = ace
#     return kilometers_dope

# laptop_profile = my_cow("ronny","mputla", location = "gauteng" , selection= "jim"  )

# print(laptop_profile)




