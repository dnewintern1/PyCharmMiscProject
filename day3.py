# age_from_user = int(input("what is your age: "))
# if age_from_user >= 65 or age_from_user <=13:
#     print("The ticket is cost is zero.")

# else:
#     print("The ticket is cost is 25$.")

# promotion = input("if you have the season pass press 'Y' if not then press 'N' : ")

# discount = 25 - (25*0.4);

# if promotion == "Y":
#     print("you get a 40% discount your ticket.new price is: ",discount )
# else:
#     print("thanks for shopping")

# planet = ["mercury" , "Venus" , "Earth" , "Jupitar" , "Saturn" , "Uranus" , "Neptune"]

# for plan in planet:
#     print(plan)
# i = 0

# for plan in planet:
#     if plan == "Earth":
#         continue
#     print(i=i+i , plan)

# extra  challange

# n = 1

# for plan in planet:
#     print(n, plan)
#     n +=1


# n = 0

# while n < 11:
#     if n%2 == 0:
#         if(n==4):
#             break
#         else:
#             print(n)
#             n +=1

#     else:
#         n +=1
#         continue


# getting introduced to range

# for n in range(10,21,2):
#     print(n)

person = {"name": "Alice", "age": 92, "email": "Alice@wonderlust@gmail.com", "Country": "UK"}

for name, details in person.items():
    print(name, ":", details)