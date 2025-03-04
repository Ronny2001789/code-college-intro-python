
name,house = ["ronny","sandton"]
plans,laptop,make_up = ["tarven","asus","condition"]

print(f"My name is {name.upper()} im  years old and at weekend im going to {plans.upper()} while using {laptop.upper()} in good {make_up.upper()}   ")

for movie in name,house,plans,laptop,make_up:
    print(movie.upper())


project = ["gyjk","igyhuj","vtyu","umi","cvb","xcvb"]
 
project.append("ronny")
print(project)

project.insert(1,"mable")
print(project)

del project[1]
print(project)


project.remove("ronny")
print(project)

project.sort(reverse = True)
print(project)

project.reverse()
print(project)

print(project[-1])

for monster in project and range(1,20,) :
    print(f"these is {project[0].upper()} and these is {project[1].upper()} and these is {project[2].upper()} and last one is{project[3].title()}")   
    print(monster)

hospital = ["car","monkey","doctor","programmer","teacher"]
print(hospital[0:4])

file = (91,2,3,4,5)
print(f"THIS IS MY GRANDMOTHER AGE {file[0]}")
