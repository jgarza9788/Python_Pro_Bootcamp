# print("""
# ___    __      __             __                 ___  __   __  
#  |  | |__)    /  `  /\  |    /  ` |  | |     /\   |  /  \ |__) 
#  |  | |       \__, /~~\ |___ \__, \__/ |___ /~~\  |  \__/ |  \                                 
# """)

print("""
___    __      __             __  
 |  | |__)    /  `  /\  |    /  ` 
 |  | |       \__, /~~\ |___ \__, 
                                  
""")

total = float(input("What was the total bill?"))
count = float(input("How many people to split the bill?"))
percentage = float(input("What percentage tip would you like to give? 10, 12,or 15?"))

result = (total * ((percentage/100) + 1.0))/count
print("Each person should pay: {0:.2f}".format(result))