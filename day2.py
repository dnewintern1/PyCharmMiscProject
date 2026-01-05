# first_name = "Radhe"
# last_name = "maurya"

# print(first_name , last_name , sep = "." , end=":")

# day = input("which day is it? ")

# days_per_week = 9
# str(days_per_week)

# int(days_per_week)

#
# fruits = ["apple", "pear", "banana", "Mango" , "peach"]
# print(fruits)
# print(fruits[2])
# print(fruits[3:5])
# fruits[0]= "orange"


# print(fruits)
# fruits.append("kiwi")
# print(fruits)
# fruits.remove("kiwi")
# print(fruits)

# ingredients = ["ham" , "bacon" , "spam" , "eggs"]
# print(ingredients)
# #
# topping = " , ".join(ingredients)
# print(topping)
#
# sentence = f"Hi can i have these {topping}"
# print(sentence)

# workweek = ("monday" , "Tuesday" , "Wednesday" , "Thursday" , "friday")
# print("exercise 1 " + workweek[0])
#
# print(workweek[3:6])
#
# print(workweek.count("Tuesday"))
#
# worktest = ("a" , "b" , "c" , "d" , "e" ,"f" ,"b")
# print(worktest.count("b"))
#
# del worktest[1]

# introduction to dictonary

# Person ={"name":"Alice" , "age" : 42 , "country" : "Wonderland"}
# print(Person)
# print(Person.keys()) #for calling all the keys there are
# print(Person.values()) #for calling all the values there are
# print(Person.items()) #to get the list of tuples

# print(Person.get("name")) #if it doesnt have any keys like that itwill crash

# #difference with lists

# colours= ["yellow" , "orange" , "red"]

# print(colours[0])

# person = {"name" : "Alice" , "age" : 42 , "email": "alice@wondere.com"}

# grades = {"French" : 75, "English": 95, "Math" : 100 ,
#      "Biology": 80}
#
# # print(grades.get("Biology"))
#
# # print(grades.keys())
# # print(grades.values())
# # print(grades.items())
#
# print(grades.keys())
# # grades.add("Drama" : 85)
# grades["Drama"] = 85
# print(grades.keys())

# total_sum = sum(grades.values())
# print(total_sum)


# getting started with sets

# chars = ["a" , "b" , "d" , "c" , "a"]
# unique_chars = set(chars)
# print(unique_chars)
# print(chars)
# print("a" in unique_chars) #introduction to in keyword

# unique_chars.add("s")
# print(unique_chars)

# unique_chars.remove("s")
# print(unique_chars)
# #print(len.chars)


# names = ["Deobrah" , "john", "tyler" , "Linda" , "Douglas" , "jessica" , "tyler" , "john" , "danieel" , "jessica"]

# unique_name = set(names)

# print(unique_name)

# print("duplicatate", len(names) - len(unique_name))
# #print(duplicatate)

# # names.add("radhe")
# # print(list.names)

# from collections import Counter

# Counter(names).most_common(3)

# try / except #invalid syntax error


# try:
#     age = int(input("how is this true only give no.s : "))
#     print("your age is " , age)

# except Valueerror:
#     print("please enter a no.")

# try:
#     x = int(input("please enter a (non-zero) number: "))
#     print("The outcome is ", 100 / x)
# except ZeroDivisionError:
#     print("Ooops! the was some issue. try again ")

