#qno1
num = [i for i in range(1, 51) if i % 3 == 0]

print(num)
print(len(num))

#qno2
words = ["python","fun","java","ai","data analysis","practice","patience","go"]

result = list(filter(lambda x: len(x) > 5, words))
print(result)

#qno3
def calculate_tax(*salaries):
    try:
        taxes = list(map(lambda x: x * 0.10, salaries))
        return sum(taxes)

    except TypeError:
        print("Salary must be numeric")

    except Exception as e:
        print("Error:", e)


print(calculate_tax(1000,2000,3000))

#qno4
celsius = [20,40,60,80]

fahrenheit = list(map(lambda c:(c*9/5)+32,celsius))

high = list(filter(lambda x:x>100,fahrenheit))

print(fahrenheit)
print(high)

#qno5
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

gen = fibonacci(10)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
























#qno6

#A
#student_utils.py
def calculate_average(*marks):
    return sum(marks)/len(marks)

def get_grade(avg,pass_mark=40):

    if avg>=80:
        return "A"

    elif avg>=60:
        return "B"

    elif avg>=pass_mark:
        return "C"

    else:
        return "F"

#B--------------------------------------------------------------
#main program



#c
#report to a text file 'report.txt'
report = open("report.txt", "w")

for student in students:

    report.write(
        f"Name: {student['name']} | Average: {student['average']:.2f} | Grade: {student['grade']}\n"
    )

report.close()

#D
#Also save all student data to a JSON file 'students.json' 

import json

with open("students.json", "w") as file:

    json.dump(students, file)

#E
#Read back both files and print their contents to the console

print("Contents of report.txt")

with open("report.txt", "r") as file:
    print(file.read())

print()

print("Contents of students.json")

with open("students.json", "r") as file:
    print(json.load(file))

#F
# Use readlines() to read 'report.txt' line by line and print each line with its
#line number 

with open("report.txt", "r") as file:

    lines = file.readlines()

    for i, line in enumerate(lines,start=1):

        print(i, line)

#qno7

#A
products = [

    {"name":"Phone","price":40000,"category":"Electronics","quantity":5},

    {"name":"Mouse","price":600,"category":"Electronics","quantity":10},

    {"name":"Keyboard","price":1200,"category":"Electronics","quantity":3},

    {"name":"Chair","price":3500,"category":"Furniture","quantity":2},

    {"name":"Table","price":8000,"category":"Furniture","quantity":0},

    {"name":"Bottle","price":300,"category":"Kitchen","quantity":20}

]

#B
def low_stock(products, threshold=5):

    for product in products:

        if product["quantity"] < threshold:

            yield product


print("Low Stock Products")

for item in low_stock(products):

    print(item)

#C

def expensive_items(products, min_price=1000):

    for product in products:

        if product["price"] > min_price:

            yield product


print("Expensive Products")

for item in expensive_items(products):

    print(item)

#D

electronics = [

    product["name"].upper()

    for product in products

    if product["category"] == "Electronics"

]

print(electronics)

#E

updated_products = list(
    map(
        lambda product: {
            **product,
            "price": product["price"] * 1.10
        },
        products
    )
)
print(updated_products)

#F

in_stock = list(
    filter(
        lambda product: product["quantity"] > 0,
        updated_products
    )
)
print(in_stock)

#G----------------------------------------------------------


#H
import json

with open("inventory.json", "w") as file:

    json.dump(updated_products, file, indent=4)

with open("inventory.json", "r") as file:

    data = file.read()
    print(data)
    print("Total Characters =", len(data))


