#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
each_person_pay_with_tip = format(round((bill / number_of_people) * (1 + percentage_tip / 100), 2), ".2f") # each_person_pay_with_tip = (tip / 100 * bill + bill) / number_of_people
print(f"Eache person should pay: ${each_person_pay_with_tip}") 