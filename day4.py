12
age_from_user = int(input("what is your age: "))
if age_from_user >= 65 or age_from_user <= 13:
    print("The ticket is cost is zero.")

else:
    print("The ticket is cost is 25$.")

promotion = input("if you have the season pass press 'Y' if not then press 'N' : ")

discount = 25 - (25 * 0.4);

if promotion == "Y":
    print("you get a 40% discount your ticket.new price is: ", discount)
else:
    print("thanks for shopping")