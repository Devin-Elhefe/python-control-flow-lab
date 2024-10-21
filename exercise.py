# Exercise 0: Example

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

# Exercise 1: Vowel or Consonant

#def check_letter():
#   letter = input("Please enter a letter (a-z or A-Z): ").lower()

#    if len(letter) != 1 or not letter.isalpha():
#        print("Invalid input. Please enter a single letter.")

#    vowels = 'aeiou'

#    if letter in vowels:
#        print(f"The letter {letter} is vowel.")
#    else:
#        print(f"The letter {letter} is a consonant.")
    
#check_letter()


# Exercise 2: Old enough to vote?

#def check_voting_eligibility():
#    try:
#        age = int(input("Please enter your age: "))

#        if age < 0:
#            print("Invalid input. Age cannot be negative.")
#        else:
#            voting_age = 18
#            if age >= voting_age:
#                print("You are eligible to vote.")
 #           else:
#                print("You are not old enough to vote.")
#    except ValueError:
#        print("Invalid input. Please enter a valid number for age.")

#check_voting_eligibility()

# Exercise 3: Calculate Dog Years

#def calculate_dog_years():
#    try:
#        dog_age = int(input("Input a dog's age: "))

#        if dog_age < 0:
#            print("Invalid input. Age cannot be a negative.")
#        elif dog_age == 1:
#            dog_years = 10
#        elif dog_age == 2:
#            dog_years = 20
#        else:
#            dog_years = 20 + (dog_age - 2) * 7

#        print(f"The dog's age in dog years is {dog_years}.")
#    except ValueError:
#        print("Invalid input. Please enter a valid number for the dog's age.")

#calculate_dog_years()

# Exercise 4: Weather Advice

#def weather_advice():
#    cold = input("Is it cold? (yes/no): ").strip().lower()
#    raining = input("Is it raining? (yes/no): ").strip().lower()

#    if cold == 'yes' and raining == 'yes':
#        print("Wear a waterproof coat.")
#   elif cold == 'yes' and raining == 'no':
#        print("Wear a warm coat.")
#    elif cold == 'no' and raining == 'yes':
#        print("carry an umbrella.")
#    elif cold == 'no' and raining == 'no':
#        print("Wear light clothing.")
#    else:
#        print("Ivalid input. Please answer with 'yes or 'no' .")

#weather_advice()

# Exercise 5: What's the Season?

def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    try:
        day = int(input("Enter the day of the month: "))

        if month not in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
            print("Invalid month entered.")
            return

        if day < 1 or day > 31:
            print("Invalid day entered.")
            return
        
        if (month == 'Dec' and day >= 21) or month in ['Jan', 'Feb'] or (month == 'Mar' and day <= 19):
            season = "Winter"
        elif (month == 'Mar' and day >= 20) or month in ['Apr', 'May'] or (month == 'Jun' and day <= 20):
            season = "Spring"
        elif (month == 'Jun' and day >= 21) or month in ['Jul', 'Aug'] or (month == 'Sep' and day <= 21):
            season = "Summer"
        elif (month == 'Sep' and day >= 22) or month in ['Oct', 'Nov'] or (month == 'Dec' and day <= 20):
            season = "Fall"
        else:
            print("Invalid date entered.")
            return

        print(f"{month} {day:02d} is in {season}.")
    except ValueError:
        print("Invalid input. Please enter a valid day as a number.")

determine_season()