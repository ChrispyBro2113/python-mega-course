day_hours = 24
week_days = 7

week_hours = day_hours * week_days

print(week_hours)

x = 10
y = '10'
z = 10.1

sum1 = x + x 
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

tuple_example = (9.1, 8.8, 7.5)
monday_temperatures = [9.1, 8.8, 7.5]
students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(students_grades.values())
length = len(students_grades)
mean = mysum / length
print(mean)


def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean



print(mean(monday_temperatures))

print(type(mean), type(sum))


def weather_condition(temperature):
    temp = float(temperature)
    if temp > 7:
        return "Warm"
    else:
        return "Cold"

print(weather_condition(5))

#user_input = input("Enter temperature:").lower()
#print(weather_condition(user_input))

#first way to do it with a for loop 
for temperature in monday_temperatures:
    print(round(temperature))

#long way to do it 
print(round(monday_temperatures[0]))
print(round(monday_temperatures[1]))
print(round(monday_temperatures[2]))

#more examples strings are treated as an array/list 
#each letter being an index 
for letter in 'hello':
    print(letter.title())

#iterate through a dictionary 
#for grades in students_grades.items():
#for grades in students_grades.keys():
for grades in students_grades.values():
    print(grades)


#while loop #
username = ''

#infinite loop unless user enters pypy
#while username != "pypy":
    #username = input("Enter username:")

#more control of the work flow
#while True:
    #username = input("Enter username:")
    #if username == 'pypy':
        #break
    #else:
        #continue


#temps = [221, 234, 340, 230]

#for temp in temps:
    #new_temps.append(temp / 10)

#print(new_temps) 

## faster way
#this is a list comprehension
#new_temps = [temp / 10 for temp in temps]
#print(new_temps)

temps = [221, 234, 340, -9999, 230]
#this is a conditional list comprehension 
#new_temps = [temp / 10 for temp in temps if temp != -9999]

#version that changes -9999 to a zero, the formating will need to be rearranged 
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps ]

print(new_temps)






