population = {'india': 136, 
              'china': 143,
              'usa': 32,
              'pakistan': 21
}

def add():
    country = input("enter the name of the country to add : ")
    country = country.lower()
    if country in population:
        print("country already exist in our dataset. terminating")
        return
    p = float(input(f"enter population for {country}"))
    population[country]=p
    print_all()

def remove():
    country = input("enter the country name to remove : ")
    country = country.lower()
    if  country not in population:
        print("country doesn't exist in our databset. terminating")
        return
    del population[country]
    print_all()

def query():
    country = input("enter the contry name to query : ")
    country = country.lower()
    if country not in population:
        print("country doesn't exist in our dataset. terminating : ")
        return 
    print(f"polulation of {country} is: {population[country]} crore")

def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")

def main():
    op=input("enter operation (add, remove, query or print):")
    if op.lower()== 'add':
        add()
    elif op.lower()== 'remove':
        remove()
    elif op.lower()== 'query':
        query()
    elif op.lower()== 'print':
        print_all()

if __name__=='__main__':
    main()
