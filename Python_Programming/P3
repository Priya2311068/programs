import statistics

stocks = {'ril' : [123, 456, 345],
          'info' : [312, 354, 200],
          'mtl': [210, 900, 400]
}

def print_all():
    for stock, price_list in stocks.items():
        avg = statistics.mean(price_list)
        print(f"for stock {stock} having price {price_list} its avg is : ",round(avg, 2))

def add():
    s = input("Enter a stock ticker to add : ")
    p = float(input("Enter the price for the stock : "))
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]



import math

def calculate_circle(radius):
    area = math.pi*(radius**2)
    circumference = math.pi*radius*2
    diameter = 2*radius
    return area, circumference, diameter

def main():
    r = float(input("Enter the radius for circle : "))
    a, c, d = calculate_circle(r)
    print(f"area {a}, circumference {c}, diameter {d}")

main()
    
