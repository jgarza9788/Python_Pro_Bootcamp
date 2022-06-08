# Python_Pro_Bootcamp

[🔗 link to Udemy Bootcamp](https://www.udemy.com/course/100-days-of-code/learn/lecture/23154980?start=15#overview)

[🔗 Coding Rooms](https://app.codingrooms.com/management/courses/6387/questions)

## Section 1: Day 1 - Beginner - Working with Variables in Python to Manage Data

### 1.1  main.py
```
#Write your code below this line 👇
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
```
>Day 1 - Python Print Function  
The function is declared like this:  
print('what to print')

### 1.2 main.py
```
#Fix the code below 👇

print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")
```


#### fixed ⭐
```
#Fix the code below 👇

print('Day 1 - String Manipulation')
print('String Concatenation is done with the \"\+\" sign.')
print('e.g. print("Hello " + "world")')
print('New lines can be created with a backslash and n.')
```

### 1.3 main.py
```python
#Write your code below this line 👇

name = input("What is your name?\n")
print(len(name))
```

### 1.4 main.py
```python
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# t is for temp
t = a 
a = b
b = t

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
```


## Section 2: Day 2 - Beginner - Understanding Data Types and How to Manipulate Strings

### 2.1 main.py
```python
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

num_list = []
for c in two_digit_number:
    num_list.append(int(c))

# bad instructions ... makes you think the output should be the equation also
# print('{0} + {1} = {2}'.format(num_list[0],num_list[1],sum(num_list)))
print(sum(num_list))
```

### 2.2 main.py
```python
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
w = float(weight)
h = float(height)
print(int(w/(h*h)))
```

### 2.3 main.py
```python
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
```


## Section 3: Day 3 - Beginner - Control Flow and Logical Operators

### 3.1 main.py
```python
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_type = ''
if number % 2 == 0:
    num_type = 'even'
else:
    num_type = 'odd'

print('This is an {num_type} number.'.format(num_type=num_type))

```

### 3.2 main.py
```python
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import math

bmi = math.ceil(weight/ (height*height))

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}, you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')
```

### 3.4 main.py
```python
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if year % 4 == 0:
    print('Leap year.')
else:
    print('Not leap year.')

```

### 3.4 main.py
```python
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

size_choice = {
    'S': 15,
    'M': 20,
    'L': 25
    }

add_pepperoni_choice = {
    'S': {'Y': 2,'N':0},
    'M': {'Y': 3,'N':0},
    'L': {'Y': 3,'N':0}
}

extra_cheese_choice = {
    'S': {'Y': 1,'N':0},
    'M': {'Y': 1,'N':0},
    'L': {'Y': 1,'N':0}
}

total = 0 
total += size_choice[size]
total += add_pepperoni_choice[size][add_pepperoni]
total += extra_cheese_choice[size][extra_cheese]

print('Your final bill is: $' + str(total) + '.')
```

### 3.5 main.py
```python
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


both_names = name1 + name2 
both_names = both_names.upper()

n1 = 0
for bn in both_names:
    for l in 'TRUE':
        if bn == l:
            n1 += 1

n2 = 0
for bn in both_names:
    for l in 'LOVE':
        if bn == l:
            n2 += 1

# n1 * = 10 #nah... i'll do it as a string
total = int(str(n1) + str(n2))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")



```


## Section 4: Day 4 - Beginner - Randomisation and Python Lists

### 4.1 main.py
```python
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random	

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇

if random.randint(0,1) == 1:
    print('Heads')
else:
    print('Tails')
```

### 4.2 main.py
```python
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n = random.randint(0,len(names)-1)
print("{0} is going to buy the meal today!".format(names[n]))
```

### 4.3 main.py
```python
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# print(int(position[0]))
# print(int(position[1]))
map[int(position[1])-1][int(position[0])-1] ='X'


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
```

## Section 5: Day 5 - Beginner - Python Loops

### 5.1 main.py
```python
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇


print(round(sum(student_heights)/len(student_heights)))


```

### 5.2 main.py
```python
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


max_score = max(student_scores)
print(f"The highest score in the class is: {max_score}")


```

### 5.3 main.py
```python
#Write your code below this row 👇

print(sum(list(range(2,101,2))))
```

### 5.4 main.py
```python
#Write your code below this row 👇

for i in range(1,101):

    if i % 3 == 0 and  i % 5 == 0:
        print('FizzBuzz')
        continue;

    if i %3 == 0:
        print('Fizz')
        continue;
    
    if i%5 == 0:
        print('Buzz')
        continue;

    print(i)
    

```


## Section 6: Day 6 - Beginner - Python Functions & Karel
## Section 7: Day 7 - Beginner - Hangman
## Section 8: Day 8 - Beginner - Function Parameters & Caesar Cipher

### 8.1 main.py
```python
```

### 8.2 main.py
```python
```

## Section 9: Day 9 - Beginner - Dictionaries, Nesting and the Secret Auction

### 9.1 main.py
```python
```

### 9.2 main.py
```python
```

## Section 10: Day 10 - Beginner - Functions with Outputs

### 10.1 main.py
```python
```

## Section 11: Day 11 - Beginner - The Blackjack Capstone Project
## Section 12: Day 12  - Beginner - Scope & Number Guessing Game
## Section 13: Day 13 - Beginner - Debugging: How to Find and Fix Errors in your Code

### 13.1 main.py
```python
```

### 13.2 main.py
```python
```

### 13.3 main.py
```python
```

## Section 14: Day 14 - Beginner - Higher Lower Game Project
## Section 15: Day 15 - Intermediate - Local Development Environment Setup & the Coffee Machine
## Section 16: Day 16  - Intermediate - Object Oriented Programming (OOP)
## Section 17: Day 17 - Intermediate - The Quiz Project & the Benefits of OOP
## Section 18: Day 18 - Intermediate - Turtle & the Graphical User Interface (GUI)
## Section 19: Day 19 - Intermediate - Instances, State and Higher Order Functions
## Section 20: Day 20 - Intermediate - Build the Snake Game Part 1: Animation & Coordinates
## Section 21: Day 21 - Intermediate - Build the Snake Game Part 2: Inheritance & List Slicing
## Section 22: Day 22 - Intermediate - Build Pong: The Famous Arcade Game
## Section 23: Day 23 - Intermediate - The Turtle Crossing Capstone Project
## Section 24: Day 24 - Intermediate - Files, Directories and Paths
## Section 25: Day 25 - Intermediate - Working with CSV Data and the Pandas Library
## Section 26: Day 26 - Intermediate - List Comprehension and the NATO Alphabet

### 26.1 main.py
```python
```

### 26.2 main.py
```python
```

### 26.3 main.py
```python
```

### 26.4 main.py
```python
```


## Section 27: Day 27 - Intermediate - Tkinter, *args, **kwargs and Creating GUI Programs
## Section 28: Day 28 - Intermediate - Tkinter, Dynamic Typing and the Pomodoro GUI Application
## Section 29: Day 29 - Intermediate - Building a Password Manager GUI App with Tkinter
## Section 30: Day 30 - Intermediate - Errors, Exceptions and JSON Data: Improving the Password

### 30.1 main.py
```python
```

### 30.2 main.py
```python
```

## Section 31: Day 31 - Intermediate - Flash Card App Capstone Project
## Section 32: Day 32 - Intermediate+ Send Email (smtplib) & Manage Dates (datetime)
## Section 33: Day 33 - Intermediate+ API Endpoints & API Parameters - ISS Overhead Notifier
## Section 34: Day 34 - Intermediate+ API Practice - Creating a GUI Quiz App
## Section 35: Day 35 - Intermediate+ Keys, Authentication & Environment Variables: Send SMS
## Section 36: Day 36 - Intermediate+ Stock Trading News Alert Project
## Section 37: Day 37 - Intermediate+ Habit Tracking Project: API Post Requests & Headers
## Section 38: Day 38 - Intermediate+ Workout Tracking Using Google Sheets
## Section 39: Day 39 - Intermediate+ Capstone Part 1: Flight Deal Finder
## Section 40: Day 40 - Intermediate+ Capstone Part 2: Flight Club
## Section 41: Day 41 - Web Foundation - Introduction to HTML
## Section 42: Day 42 - Web Foundation - Intermediate HTML
## Section 43: Day 43 - Web Foundation - Introduction to CSS
## Section 44: Day 44 - Web Foundation - Intermediate CSS
## Section 45: Day 45 - Intermediate+ Web Scraping with Beautiful Soup
## Section 46: Day 46 - Intermediate+ Create a Spotify Playlist using the Musical Time Machine
## Section 47: Day 47 - Intermediate+ Create an Automated Amazon Price Tracker
## Section 48: Day 48 - Intermediate+ Selenium Webdriver Browser and Game Playing Bot
## Section 49: Day 49 - Intermediate+ Automating Job Applications on LinkedIn
## Section 50: Day 50 - Intermediate+ Auto Tinder Swiping Bot
## Section 51: Day 51 - Intermediate+ Internet Speed Twitter Complaint Bot
## Section 52: Day 52 - Intermediate+ Instagram Follower Bot
## Section 53: Day 53 - Intermediate+ Web Scraping Capstone - Data Entry Job Automation
## Section 54: Day 54 - Intermediate+ Introduction to Web Development with Flask

### 54.1 main.py
```python
```

## Section 55: Day 55 - Intermediate+ HTML & URL Parsing in Flask and the Higher Lower Game

### 55.1 main.py
```python
```

## Section 56: Day 56 - Intermediate+ Rendering HTML/Static files and Using Website Templates
## Section 57: Day 57 - Intermediate+ Templating with Jinja in Flask Applications
## Section 58: Day 58 - Web Foundation Bootstrap
## Section 59: Day 59 - Advanced - Blog Capstone Project Part 2 - Adding Styling
## Section 60: Day 60 - Advanced - Make POST Requests with Flask and HTML Forms
## Section 61: Day 61 - Advanced - Building Advanced Forms with Flask-WTForms
## Section 62: Day 62 - Advanced - Flask, WTForms, Bootstrap and CSV - Coffee & Wifi Project
## Section 63: Day 63 - Advanced - Databases and with SQLite and SQLAlchemy
## Section 64: Day 64 - Advanced -My Top 10 Movies Website
## Section 65: Day 65 - Web Design School - How to Create a Website that People will Love
## Section 66: Day 66 - Advanced - Building Your Own API with RESTful Routing
## Section 67: Day 67 - Advanced - Blog Capstone Project Part 3 - RESTful Routing
## Section 68: Day 68 - Advanced - Authentication with Flask
## Section 69: Day 69 - Advanced - Blog Capstone Project Part 4 - Adding Users
## Section 70: Day 70 - Advanced - Deploying Your Web Application with Heroku
## Section 71: Day 71 - Advanced - Data Exploration with Pandas: College Major v.s. Your Salary
## Section 72: Day 72 - Advanced - Data Visualisation with Matplotlib: Programming Languages
## Section 73: Day 73 - Advanced - Aggregate & Merge Data with Pandas: Analyse the LEGO Dataset
## Section 74: Day 74 - Advanced - Google Trends Data: Resampling and Visualising Time Series
## Section 75: Day 75 - Advanced - Beautiful Plotly Charts & Analysing the Android App Store
## Section 76: Day 76 - Advanced - Computation with NumPy and N-Dimensional Arrays
## Section 77: Day 77 - Advanced - Linear Regression and Data Visualisation with Seaborn
## Section 78: Day 78 - Advanced - Analysing the Nobel Prize with Plotly, Matplotlib & Seaborn
## Section 79: Day 79 - Advanced - The Tragic Discovery of Handwashing: t-Tests & Distributions
## Section 80: Day 80 - Advanced - Capstone Project  - Predict House Prices
## Section 81: Day 81 - Professional Portfolio Project - [Python Scripting]
## Section 82: Day 82 - Professional Portfolio Project - [Python Web Development]
## Section 83: Day 83 - Professional Portfolio Project - [Python Scripting]
## Section 84: Day 84 - Professional Portfolio Project - [GUI]
## Section 85: Day 85 - Professional Portfolio Project - [GUI]
## Section 86: Day 86 - Professional Portfolio Project - [Game]
## Section 87: Day 87 - Professional Portfolio Project - [Web Development]
## Section 88: Day 88 - Professional Portfolio Project - [Web Development]
## Section 89: Day 89 - Professional Portfolio Project - [GUI Desktop App]
## Section 90: Day 90 - Professional Portfolio Project - [HTTP Requests & APIs]
## Section 91: Day 91 - Professional Portfolio Project - [Image Processing & Data Science]
## Section 92: Day 92 - Professional Portfolio Project - [Web Scraping]
## Section 93: Day 93 - Professional Portfolio Project - [GUI Automation]
## Section 94: Day 94 - Professional Portfolio Project - [Game]
## Section 95: Day 95 - Professional Portfolio Project - [HTTP Requests & APIs]
## Section 96: Day 96 - Professional Portfolio Project - [Web Development]
## Section 97: Day 97 - Professional Portfolio Project - [Python Automation]
## Section 98: Day 98 - Professional Portfolio Project - [Data Science]
## Section 99: Day 99 - Professional Portfolio Project - [Data Science]
## Section 100: Day 100 - Professional Portfolio Project - [Data Science]
## Section 101: Final Stretch


