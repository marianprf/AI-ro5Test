


#Exercise 1: Grade Classification
#Write a program that asks the user for a grade (a number between 0 and 100) and prints the corresponding letter grade:

#90 or above → "A"

#80 to 89 → "B"

#70 to 79 → "C"

#60 to 69 → "D"

#Below 60 → "F"



grade = int(input("Enter your grade(0 to 100): "))

if grade < 0 or grade > 100:
    print("Invalid! Please enter a number between 0 and 100.")
else:
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")


#Exercise 2: Temperature Check
#Write a program that asks the user to input the current temperature in Celsius and prints:

#"It's freezing!" if the temperature is below 0°C.

#"It's cold!" if the temperature is between 0 and 15°C.

#"It's warm!" if the temperature is between 16 and 25°C.

#"It's hot!" if the temperature is above 25°C.

temp = int(input("Input Temperature: "))
if temp <= 0:
    print("it's freezing!")
elif temp <= 15:
    print("It's cold!")
elif temp <= 25:
    print("It's warm!")
else:
    print("It's Hot!")


#Exercise 3: Voting Eligibility
#Write a program that checks if a person is eligible to vote. The person is eligible if their age is 18 or above. The program should:

#Ask the user for their age.

#Print "You are eligible to vote." if the age is 18 or older.

#Print "You are not eligible to vote." if the age is under 18.

age = int(input("Enter age here: "))
if age < 18:
    print("You are not eligible to vote.")
else:
    print("You are eligible to vote!")



#Exercise 4: Even or Odd Number
#Write a program that checks if a number is even or odd.

#If the number is divisible by 2 (remainder is 0), print "The number is even."

#If the number is not divisible by 2 (remainder is not 0), print "The number is odd."

number = int(input("Insert number here: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("Number is odd")


#Exercise 5: Month to Season
#Write a program that asks the user for the name of a month (e.g., "January", "March", "August") and prints the season:


#"Winter" for December, January, or February.

#"Spring" for March, April, or May.

#"Summer" for June, July, or August.

#"Fall" for September, October, or November.
user_months = input("Input month here: ")

winter_months = ["January", "February", "March"]
spring_months = ["April", "May", "June"]
summer_months = ["July", "August", "September"]
fall_months = ["October", "November", "December"]

if user_months in winter_months:
    print("Winter")
elif user_months in spring_months:
    print("Spring")
elif user_months in summer_months:
    print("Summer")
elif user_months in fall_months:
    print("Fall")
else:
    print("That's not a valid month.")


#Exercise 6: Age Group Categorization
#Write a program that takes a user's age and determines their age group:

#"Child" if the age is between 0 and 12.

#"Teenager" if the age is between 13 and 17.

#"Adult" if the age is between 18 and 64.

#"Senior" if the age is 65 or older.

user_age = int(input("Input age here: "))
if user_age in range(0,12):
    print("Child")
elif user_age in range(13,17):
    print("Teenager")
elif user_age in range(18,46):
    print("Adult")
else:print("Senior")


#Exercise 7: Discount Eligibility
#Write a program that asks the user for the total amount of a purchase and prints a discount message:

#If the purchase is over $100, give a 20% discount.

#If the purchase is between $50 and $100 (inclusive), give a 10% discount.

#If the purchase is less than $50, give no discount.

total = float(input("Input total purchase amount: "))

if total >= 100:
    discount = 0.20
    print("You get 20% discount!")
elif 50 < total < 100:
    discount = 0.10
    print("You get 10% discount!")
else:
    discount = 0.0
    print("You get no discount!")

final_price = total - (total * discount)
print(f"Your final price is: ${final_price:.2f}")


#8.🧪 Exercise: Movie Ticket Price Calculator
#ask:

#Ask the user for their age and calculate the ticket price based on this rule set:


#Age Range	Ticket Price
#0–3 years	Free
#4–12 years	$8
#13–64 years	$12
#65 and above	$7


age = int(input("Input your age here: "))

if 0 <= age <= 3:
    print("Your ticket is Free!")
elif 4 <= age <= 12:
    print("Ticket price is $8")
elif 13 <= age <= 64:
    print("Ticket price is $12")
else:
    print("Ticket price is $7")



#LIST CONTROL

#Starting list:
fruits = ["apple", "banana", "cherry"]

#print whole list:
print("all fruits: " , fruits)

#Add a fruit:
fruits.append("orange")
print("After adding orange:" , fruits)

#Remove a fruit:
fruits.remove("banana")
print("After removing banana: ", fruits)

#Acces to a specific item:
print("First fruit:",fruits[0])

#Change a fruit
fruits[1] = "grape"
print("After changing the second fruit: " , fruits)






#Rock, scissors, paper game:

# Get the player's choice
user_input = input("Choose rock, scissors, or paper: ").lower()
#import random
import random
# List of choices
choices = ["rock", "scissors", "paper"]

# Get the computer's random choice
computer_choice = random.choice(choices)

# Print the choices
print(f"Computer chose: {computer_choice}")

# Compare choices and determine the winner
if user_input == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_input == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_input == "paper" and computer_choice == "rock":
    print("You win!")
elif user_input == computer_choice:
    print("It's a tie!")
else:
    print("You lose! ")


#Guess the number game:
import random
secret_number = random.randint(1,10)
user_guess = int(input("Guess the number: "))
tries = 1
while user_guess != secret_number:
    if user_guess > secret_number:
        print("It's too high , try again!")

    elif user_guess < secret_number:
        print("It's too low, try again!")
    user_guess = int(input("Guess the number: "))
    tries += 1
else:
    print(f"You got it!, both players chose {user_guess}, you got it in {tries} tries!" )


while True:  # This will keep running until we get a valid password
    password = input("Enter your password: ")  # Ask the user for their password

    # Check if the password is too short
    if len(password) < 8:
        print("Your password is too short! Try again.")
        continue  # Start the loop over and ask for the password again

    # Check if the password contains at least one number
    has_digit = False  # Start by assuming there's no digit in the password
    for char in password:  # Loop through each character in the password
        if char.isdigit():  # Check if the character is a number
            has_digit = True  # If we find a digit, we change has_digit to True
            break  # No need to check any more characters once we find a digit

    # If there's no digit in the password, tell the user to try again
    if not has_digit:
        print("Your password must contain at least one number. Try again.")
        continue  # Start the loop over and ask for the password again

    # If the password passed all checks, it's valid, so we break out of the loop
    print("Password is strong enough!")
    break  # Exit the loop because we have a valid password









    incercari = 0
    parola = "pass123"

    while True:
        input_user = input("Introduceti parola aici: ")
        if input_user != parola:
            incercari += 1
            if incercari >= 3:
                print("Accesul interzis!")
                break
        else:
            print("Acces permis!")
            break
