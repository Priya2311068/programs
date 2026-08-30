a = int(input("Enter your birth year : ")) 
b = int(input("Enter the current year : "))
age = b - a
print(age)

first = input("Enter your first name : ")
middle = input("Enter your middle name : ")
last = input("Enter your last name : ")
full_name = first + " " + middle + " " + last
print(full_name)

length = 92
breadth = 48.8
area = length*breadth
print(area)

packets = 9
packet_cost = 1.49*80
bill = 1.49*9*80
amount = 20*80
left_money = amount - bill 
print(left_money/80)

num = 17
print("binary representation of 17 is :", format(num,'b'))

street = "A 12" 
city =  "Rohtak"
country = "India"
address = street + '\n'  + city + '\n'  + country
print(address)
print(f"address is : {street} \n {city} \n {country}")

string = "Earth revolves around the sun"
print(string[6:14])
print(string[-4:])

x = int(input("Enter how many fruits you eat daily : "))
y = int(input("enter how many veges you eat daily: "))
print(f"I eat {y} veggies and {x} fruits")

s = 'maine 200 banana khaye'
print(s)
print(s.replace('200 banana','10 samosa'))

exp = [2200, 2350, 2600, 2130, 2190]
print(2000 in exp)

exp.insert(3, 4500)
print(exp)
exp.remove(2350)
print(exp)

heros = ['spider man', 'thor' , 'hulk', 'captain america', 'iron man']
print(len(heros))
print(heros[2:4])
print(heros.sort())
print(heros)

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0 
for outcome in result:
    if outcome == "heads":
        count += 1
    else :
        continue
print(count)

for i in range(1, 11):
    if i%2 != 0:
        print(i*i)
    else :
        continue
   
for i in range(1, 11):
    if i%2 == 0:
        print(i*i)
    else :
        continue

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]
e = int(input("enter the expense of the month : "))
print(e)
month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f"you spent {e} in {month_list[i]}")
else:
    print("noo you have spent that money")
        

for i in range(5):
    print(f"you ran {i+1} miles")
    tired = input("are you tired? : ")
    if tired == 'yes':
        break

if i == 4:
    print("""hurry!
           you are rock star!
           you just finished 5kmbrace!""")
else:
    print("""you didn't finish 5km race " 
    "but hey congrats anyways! you still ran {i+1}miles""")

for i in range(1, 6):
    print(i*'*')

def calculate_area(b, h):
    area = 1/2*b*h
    print(area)

calculate_area(4, 5)

def calculate_area(l, w):
    area = l*w
    print(area)

calculate_area(4, 5)

def print_pattern(n):
    for i in range(n):
        print(i*'*')

print_pattern(10)
print_pattern(8)
print_pattern(6)

population = {'china':143, 'india': 136, 'USA':32, 'Pakistan': 21}
def print_all():
    for country, p in population.items():
        print(f"{country}-->{p}")

def add():
    ask = input("Enter the name of the country : ")
    
    for country in population.keys():
        if ask == country:
            print("This country alraedy exists in the dataset!!")
            break
        else:
            pop = input("Population of entered country :  ")
            print(f"{ask}-->{pop}")

def remove():
    country = input("Enter the name of the country to remove : ")
    if country in population.keys():
        del population[country]
        print_all()       
    else:
         print("Entered country does't exists!!")
        

def query():
    country = input("enter the name of the country you have query in : ")
    if country in population.keys():
        print(population[country])
        return

if __name__ == '__main__':
    ques = input("enter what you want to do : ")
    if ques == 'add':
        add()
    elif ques == 'print':
        print_all()
    elif ques == 'remove':
        remove()
    elif ques == 'query':
        query()

import statistics
stocks = {"info": [600, 630, 620],
          "ril": [1430, 1490, 1567],
          "mtl": [234, 180, 160]
          }
def print_all():
    for stock ,price in stocks.items():
        avg = statistics.mean(price)
        print(f"{stock}==>{price}==> avg: ", round(avg,2))

def add():
    s = input("enter the stock name : ")
    p = (input("enter the prices for the stock : "))
    p = float(p)
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    print_all()


if __name__ == '__main__':
    enter = input("enter what u wanna do : ")
    if enter == 'print':
        print_all()
    elif enter == 'add':
        add()    

import math
def calculate_area(r):
    area = math.pi*r*r
    circumference = 2*math.pi*r
    diameter = 2*r
    print(area)
    print(circumference)
    print(diameter)

if __name__ == '__main__':
    calculate_area(7)


import sys
sys.path.append("C:\Code")
import function as f

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID is {self.id} \n Name : {self.name}")

emp = Employee(1, "coder")
emp.display()

del emp.id

try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display()
except NameError:
    print("emp is not defined")


class Animal:

    def __init__(self, habit):
        self.habit = habit

    def print_habit(self):
        print(f"habit of this animal is : {self.habit}")
    
    def sound(self):
        print("some animal sound ")

class Dog(Animal):

    def __init__(self):
        super().__init__("Kennel")     

    def sound(self):
        print("woof woof !")

         
x = Animal('bark')
x.print_habit()
x.sound()


class Teacher:
    def teacher_action(self):
        print("I can teach")

class engineer:
    def engineer_action(self):
        print("I can write codes")

class youtuber:
    def youtuber_action(self):
        print("I can code and teach")

class person(Teacher, engineer, youtuber):
    pass
    

coder = person()
coder.teacher_action()
coder.engineer_action()
coder.youtuber_action()

class AdultException(Exception):
    pass

class Person:
    def __init__(self, n, age):
        self.name = n
        self.age = age
    def get_minor_age(self):
        if int(self.age) >= 18:
            raise AdultException
        else:
            return self.age
        
    def display(self):
        try:
            print(f"age--> {self.get_minor_age()}")
        except AdultException:
            print("Person is an adult")
        finally:
            print(f"name-> {self.name}")

person = Person("priya", 6)
person.display()


def swap(a, b, arr):
    if a != b:
       temp = arr[a]
       arr[a] = arr[b]
       arr[b] = temp

def partition_func(start, end, elements):

    pivot_index = start
    pivot = elements[pivot_index]


    while start < end :

        while elements[start] <= pivot and start < len(elements):
            start += 1

        while elements[end] > pivot :
            end -= 1

        if start < end :
            swap(start, end, elements )
    
    swap(pivot_index, end, elements)    
    return end

def quick_sort(start, end, elements):
    if start < end:
        pi = partition_func(start, end, elements)
        quick_sort(start, pi-1, elements)
        quick_sort(pi+1, end, elements)
    


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    quick_sort(0, len(elements) - 1, elements)
    print(elements)

def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = i
        j = i-1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = anchor


if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)
 
def merge_sort(arr, key = ' None'):
    if len(arr) <= 1:
        return
     
    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]  

    merge_sort(left, key = 'None')
    merge_sort(right, key = 'None')

    merge_two_sorted_list(left, right, arr, key = 'None')

def merge_two_sorted_list(a, b, arr, key = ' None'):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i][key] < b[j][key]:
            arr[k][key] = a[i][key]
            i += 1

        else:
            arr[k][key] = b[j][key]
            j += 1
        k+= 1

    while i < len_a:
        arr[k][key] = a[i][key]
        i += 1
        k+=1

    while j < len_b:
        arr[k][key] = b[j][key]
        j += 1
        k+=1

if __name__ == '__main__':
    elements = [
#         { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    merge_sort(elements, key = 'time_hour')
    print(f"the sorted array is : {elements} ")


months = ['jan', 'feb', 'mar', 'apr', 'may']
expense = [2200, 2350, 2600, 2130, 2190]

print(expense[1] - expense[0])
print(2000 in expense)


class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        llist = ''
        while current:
            llist += str(current.data) + '-->' if current.next else str(current.data)
            current = current.next
        print(llist)

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def get_length(self):
        current = self.head
        count = 0 
        while current:
            count += 1
            current = current.next
        return count

    def insert_at_index(self, index):
        if index <0 or index > self.get_length():
            print("Index out of bounds")
            return
        new_node = node(input('enter the data to insert : '))
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def remove_at_index(self, index):
        if index < 0 or index > self.get_length():
            print('index out of bounds')
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        if current.next is None:
            print("No Node at this index")
            return
        current.next = current.next.next

    def insert_after_value(self, value):
        new_node = node(input('enter the data to insert : '))
        current = self.head
        while current:
            if current.data == value:
                current,next = new_node
                new_node.next = current.next
                return

if __name__ == '__main__':
    llist = linked_list()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)
    llist.print_list()
    llist.insert_at_index(2)
    llist.print_list()
    llist.remove_at_index(3)
    llist.print_list()
    llist.insert_after_value(5)
    llist.print_list()

