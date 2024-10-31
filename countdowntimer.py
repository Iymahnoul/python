import time
from datetime import datetime
def countdowntimer(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end ='\r')
        time.sleep(1)
        time_sec -= 1
    print("stop")
#countdowntimer(2400) #countdown for 40 minutes
def letterPattern():
    for n in range(10):
        print('A', end='')
    for n in range(8):
        print('B', end='')
    for n in range(4):
        print('CD', end='')
    print('E', end='')
    for n in range(6):
        print('F', end='')
    print("G")

def fibonacci():
    fib_num = eval(input("please enter number of fibonacci series:"))
    a,b = 1,1
    empty_list = []
    empty_list.append(a)
    empty_list.append(b)
    for x in range(fib_num):
        c = empty_list[x] + empty_list[x+1]
        empty_list.append(c)

    for x in range(len(empty_list)):
        print(str(empty_list[x])+",", end=" ")
#fibonacci()

def rectangle(rect_height, rect_width):
    rect_height = eval(input("enter rectangle height"))
    rect_width = eval(input("enter rectangle width"))
    for x in range(rect_height):
        print("*" * rect_width)
#rectangle()

def hollow_rectangle(rect_height, rect_width):
    rect_height = eval(input("enter rectangle height"))
    rect_width = eval(input("enter rectangle width"))
    for x in range(rect_height):
        if x == 1 or x == 2:
            print("*", " " * (rect_width-4), "*")
        else:
            print("*" * rect_width)

def R_rightAngled():
    height = eval(input("enter triangle height"))
    width = eval(input("enter triangle width"))
    for x in range(height):
        print("* "*(x+1))

def inverted_R_rightAngled():
    height = eval(input("enter triangle height"))
    width = eval(input("enter triangle width"))
    for x in range(height):
        print("* " * width)
        width -= 1

def diamond_shape():
    size = eval(input("Enter an odd number"))
    empty_list = []
    for x in range(size + 1):
        if x % 2 != 0:
            empty_list.append(x)

    width = size
    #height =eval(input("please enter height"))
    starting_spaces = (width - 1) // 2
    starting_spaces2 = 1
    for x in range(len(empty_list)):
        print(" " * starting_spaces, "*" * empty_list[x], " " * starting_spaces)
        starting_spaces -=1
    empty_list.pop(-1)
    empty_list.reverse()
    for y in range(len(empty_list)):
        print(" " * starting_spaces2, "*" * empty_list[y], " " * starting_spaces2)
        starting_spaces2+=1

import random, math
#random.randint(x,y) imports bound integer number
#random.uniform(x,y) imports bound decimal number
#random.random() imports unbound integer number
'''x = random.uniform(1,10)
x_rand = round(x,2)
print(x, "\t", x_rand)
dir(math)'''
import math
def centimetersToInches():
    #2.54cm to an inch
    while True:
        try:
            user_centimeter_input = eval(input("please enter your value in centimeters:"))
            if user_centimeter_input < 0:
                print("input is a negative number")
            else:
                break
        except(NameError):
            print("invalid input,please enter a positive number")
    equivalent_inch = user_centimeter_input / 2.54
    print(user_centimeter_input,"is equivalent to ", round(equivalent_inch,2)," inches")


def fahCel():
    #2.54cm to an inch
    while True:
        try:
            user_temperature_input = eval(input("please enter your temperature value:"))
            break
        except(NameError):
            print("invalid input,please enter any number")
    temperature_scale = eval(input("Select temperature unit or scale:\n1.\tFahrenheit\n2.\tCelcius"))
    if temperature_scale == 1:
        celcius_equivalent = (5/9) * (user_temperature_input - 32)
        print(user_temperature_input, "Fahrenheit is equivalent to", celcius_equivalent,chr(176),"C")
    elif temperature_scale == 2:
        fahrenheit_equivalent = ((9/5) * user_temperature_input) + 32
        print(user_temperature_input, "Celcius is equivalent to", fahrenheit_equivalent, chr(176), "F")
    else:
        print("Invalid Choice, try again.")

def qty_price_discount():
    while True:
        try:
            user_quantity = eval(input("please enter number of items you wish to buy"))
            if user_quantity < 0:
                print("number can't be negative")
                user_quantity = eval(input("enter positive number of items you wish to buy"))
            break
        except(NameError):
            print("invalid input!")
    if user_quantity < 10:
        amount = 12 * user_quantity
        print("your total amount is ", "$", amount)
    elif user_quantity <= 99:
        amount = 10 * user_quantity
        print("your total amount is ", "$", amount)
    else:
        amount = 7 * user_quantity
        print("your total amount is ", "$",amount)


def multiplication_game():
    import random
    player_score = 0 # right_answer
    wrong_answer = 0
    print("Welcome user to this multiplication game.")
    player_name = input("please enter your name: ")
    print()
    for x in range(10):
        rand1 = random.randint(0,16)
        rand2 = random.randint(0, 16)
        while True:
            print("Question ", x+1," :", rand1, " X ", rand2, sep="")
            correct_answer = rand1 * rand2
            try:
                player_answer = eval(input())
                break
            except(NameError):
                print("wrong input! try again")
        if player_answer == correct_answer:
            print("Right!")
            player_score += 1
        else:
            print("Wrong!")
            wrong_answer += 1

    print("\n",player_name,", Your score is: ", player_score, sep="")
    print("You failed: ", wrong_answer, "questions")
    play_request = eval(input("\n Play again?\t1:Yes\t2:No"))
    if play_request == 1:
        multiplication_game()
    else:
        pass
############ USER INPUT DRAFT ################
'''
while True:
    try:
        user_centimeter_input = eval(input("please enter your value in centimeters:"))
        if user_centimeter_input < 0:
            print("input is a negative number")
        elif user_centimeter_input == 3:
            print("You entered three")
        else:
            break
    except(NameError):
        print("invalid input,please enter a positive number")
'''
def hourForward():
    #user_hour = eval(input("please enter any hour"))
    user_meridian_dic = {1: 'am', 2: 'pm'}
    while True:
        try:
            user_hour = eval(input("please enter positive hour "))
            if user_hour < 0:
                print("hour can't be negative")
            elif user_hour > 12:
                print("hour can't be above 12")
            else:
                #hour_advance = eval(input("how many hours do you want to advance?"))
                user_meridian = eval(input("\t1:am\t2:pm"))
                print("OK, meridian captured")
                while True:
                    try:
                        hour_advance = eval(input("how many hours do you want to advance? "))
                        if hour_advance < 0:
                            print("hour can't be negative")
                            #hour_advance = eval(input("how many hours to the future do you want to go?"))
                        elif user_hour > 12:
                            print("enter your hour between 1 - 12")
                            #user_hour = eval(input("how many hours to the future do you want to go?"))
                        else:
                            new_24hour = user_hour + hour_advance  # serves am and pm
                            new_12hour = (user_hour + hour_advance) % 12  # serves hour
                            if user_meridian == 1 and new_24hour < 12:
                                print("your old hour is: ", user_hour, user_meridian_dic[user_meridian])
                                print("your new hour is: ", new_12hour, "am")
                                break
                            elif user_meridian == 1 and new_24hour >= 12:
                                print("your old hour is: ", user_hour, user_meridian_dic[user_meridian])
                                print("your new hour is: ", new_12hour, "pm")
                                break
                            elif user_meridian == 2 and new_24hour < 12:
                                print("your old hour is: ", user_hour, user_meridian_dic[user_meridian])
                                print("your new hour is: ", new_12hour, "pm")
                                break
                            else:
                                print("your old hour is: ", user_hour, user_meridian_dic[user_meridian])
                                print("your new hour is: ", new_12hour, "am")
                                break
                    except(NameError):
                        print("Invalid Input!")
                break


        except(NameError):
            print("Invalid Input!")
            program_request = eval(input("\n Try again?\t1:Yes\t2:No"))
            while True:
                if program_request == 1:
                    hourForward()
                    break
                elif program_request == 2:
                    break
            break





def Euclid_Algorithm():
    ########## THIS PROGRAM COMPUTES THE GREATEST COMMON FACTOR OF TWO NUMBERS ########
    n1 = eval(input("enter your first number"))
    n2 = eval(input("enter your second number"))

    if n1 > n2:
        larger_num = n1
        smaller_num = n2
    else:
        larger_num = n2
        smaller_num = n1

    while smaller_num != 0:
        remainder = larger_num % smaller_num
        larger_num = smaller_num
        smaller_num = remainder
    print("the Greatest Common Divisor is", larger_num)

def non_repeated_letters():
    wordlist = ["men","zobo","kick","dive","letter","malt","dodo","cut","learn","jug"]
    for w in wordlist:
        wordsplit = w.split()
        for s in wordsplit:
            print(s[1])

def decimal_to_binary():
    bin_list = []
    num = eval(input("Please enter your number"))
    while num > 0:
        num = num // 2
        if num == 1:
            bit = 0
        elif num == 0:
            bit = 1
        else:
            bit = num % 2
        bin_list.append(bit)
    print(bin_list)
    bin_list_reverse = bin_list[::-1]
    print(bin_list_reverse)
#decimal_to_binary()

def binary_to_decimal():
    sum = 0
    bin_num = input("Please enter your binary number")
    bin_list = list(bin_num)
    bin_len = len(bin_list)
    for x in range(bin_len):
        sum = bin_list[x] * (2 ** (bin_len-1))
        sum = sum + sum
        x += 1
        bin_len -=1
    print("the binary equivalent of", bin_num, "is", sum)
#binary_to_decimal()


class Example():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

class Child(Example): # class inheritance
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return 2 * (self.a + self.b)

parent_obj = Example(4, 7)
child_obj = Child(4, 7)
print("the sum of the two numbers is:", parent_obj.add())
print("the sum of the two numbers is:", child_obj.add())
print("the product multiply by two is:", 2 * parent_obj.multiply())


class Investment():
    def __init__(self,principal, interest):
        self.principal = principal
        self.interest = (interest / 100)



    def __str__(self):
        return "principal - {},  Interest - {}%".format(self.principal, round((self.interest * 100)))

    def value_after(self,years):
        self.years = years
        return (self.principal * (1 + self.interest) ** self.years)


invest_obj = Investment(9000, 5)
print(invest_obj.__str__(), "\nwhile the investment return is valued at", invest_obj.value_after(5))


class Product():
    def __init__(self, name, amount_in_stock, price):
        self.name = name
        self.amount = amount_in_stock
        self.price = price

    def get_price(self, qty_to_buy):
        self.qty_to_buy = qty_to_buy
        actual_cost = 0
        if self.qty_to_buy < 10:
            actual_cost = (self.qty_to_buy * self.price)
            print("The actual cost for your order is ", actual_cost)
        elif self.qty_to_buy >= 10 and self.qty_to_buy <= 99:
            actual_cost = (self.qty_to_buy * self.price) * (10 / 100)
            print("The actual cost for your order is ", actual_cost)
        elif self.qty_to_buy >= 100:
            actual_cost = (self.qty_to_buy * self.price) * (20 / 100)
            print("The actual cost for your order is ", actual_cost)
        else:
            print("Quantity ordered is invalid")


    def make_purchase(self, qty_to_buy):
        self.qty_to_buy = qty_to_buy
        actual_total = 0
        if self.qty_to_buy < 10:
            actual_total = self.qty_to_buy * self.price
            discount_rate = 0
            discount = actual_total * (0/100)
            discount_price = actual_total - discount
            print("The discount Price:", discount_price)
        elif self.qty_to_buy >= 10 and self.qty_to_buy <= 99:
            actual_total = self.qty_to_buy * self.price
            discount = actual_total * (10/100)
            discount_price = actual_total - discount
            print("The discount Price:", discount_price)
        elif self.qty_to_buy >= 100:
            actual_total = self.qty_to_buy * self.price
            discount = actual_total * (20/100)
            discount_price = actual_total - discount
            print("The discount Price:", discount_price)
        else:
            print("Quantity ordered is invalid")



#prod_obj = Product("Phone", 50, 100000)
#prod_obj.get_price(67)
#prod_obj.make_purchase(67)
#R_rightAngled()



for x in range(1):
    for x in range(1):
        print("A"*10, end = '')
    for x in range(1):
        print("B" * 8, end = '')
    for x in range(1):
        print("CD" * 4, end = '')
    for x in range(1):
        print("E","F"*6,"G", end = '')


def read_file():
    try:
        fr = open("gapminder.txt", "r")
        text = fr.read()
        print(text)
        fr.close()
    except(FileNotFoundError):
        print("\nthe file doesn't exists")
    finally:
        print("complete")

#summing flexible number of arguments
def total(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)
#total(1,2,3,4,5,6,7)

multiline = '''
first line
second line 
third line'''

#print(multiline)

ten = 10
user_value=eval(input("please enter a value:"))
if ten is user_value:
    print("the values are same")
else:
    print("the values are different")

myList = [1,2.3,"Python"]
print(myList[2])
myList.insert(2,"extra")
print(myList[2])
rep_myList = myList * 10
print(rep_myList[8])

c = [10, 20, 30]
def func1(x):
    print("the value of c is ", c)

func1(c)



num1, num2 = 12, 3
quotient = num1 / num2
print("the quotient of the first number to the second number is", quotient)

class Arithmetic():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def Addition(self):
        sum = self.a + self.b
        return sum

    def Power(self):
        power = self.a ** self.b
        return power

a = Arithmetic(4,7)
print("This is the latest class and the sum is", a.Addition())
print("This is the latest class and the power is", a.Power())

odd_counter = 0
odd_list = []
even_counter = 0
even_list = []
for x in range(21):
    if x % 2 > 0:
        odd_counter = odd_counter + 1
        odd_list.append(x)
    else:
        even_counter = even_counter + 1
        even_list.append(x)

print("there are", odd_counter, "in the list you provide which are", odd_list)
print("there are", even_counter, "in the list you provide which are", even_list)

def FoulLanguage():
    foul_alert = 0
    foul_comments = []
    FoulLanguageList = ["kill", "fuck", "nonsense", "maim", "revenge", "torture", "protest"]
    user_comment = input("please write comment here...")
    user_comment_lowercase_list = user_comment.lower().split()
    for word_comment in user_comment_lowercase_list:
        if word_comment in FoulLanguageList:
            foul_alert = foul_alert + 1
            foul_comments.append(word_comment)
            
    if foul_alert > 0:
        print("Sorry, foul words", foul_comments," are not allowed on this space")
    else:
        print("your comment haas been scanned and is NOT foul")


#FoulLanguage()


















