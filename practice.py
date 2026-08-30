# class Graph:
#   def __init__(self, edges):
#     self.edges = edges
#     self.graph_dic = {}
#     for start, end in edges:
#       if start in edges:
#         self.graph_dic[start].append(end)
#       else:
#         self.graph_dic[start] = [end]
#     print("graph dic: ", self.graph_dic)

#   def get_paths(self, start, end, path = []):
#     path = path + [start]

#     if start == end:
#       return [path]

#     if start not in self.graph_dic:
#       return []

#     paths = []
#     for node in self.graph_dic[start]:
#       if node not in path:
#         new_paths = self.get_paths(node, end, path)
#         for p in new_paths:
#           paths.append(p)


#     return paths

#   def get_shortest_path(self, start, end, path = []):
#     path = path + [start]
     
#     if start == end:
#       return [path]

#     if start not in self.graph_dic:
#       return []

#     shortest_path = None
#     for node in self.graph_dic[start]:
#       if node not in path:
#         sp = self.get_shortest_path(node, end, path)
#         if sp:
#           if shortest_path is None or len(sp) < len(shortest_path):
#             shortest_path = sp

#     return shortest_path



# if __name__ == "__main__":
#   routes = [
#     ("Mumbai", "Paris"),
#     ("Mumbai", "Dubai"),
#     ("Paris", "Dubai"),
#     ("Paris", "New York"),
#     ("Dubai", "New York"),
#     ("New York", "Toronto"),

#   ]

#   route_graph = Graph(routes)

#   start = "Mumbai"
#   end = "Toronto"

#   print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
#   print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))

#   start = "Dubai"
#   end = "New York"

#   print(f"All paths between: {start} and {end}: ",route_graph.get_paths(start,end))
#   print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))


a = [1, 2, 3, 4, 5]
# print(dir(a))
# # c = a.__add__([6])
# # print(c)
# print(a.__class__)
# print(a.__iadd__([6]))
# print(a.__mul__(2))
# print(a.__rmul__(2))
# print(a.__sizeof__())
# print(a.__str__())
# print(a.__repr__())
# print(a.__len__())
# print(a.__contains__(3))
# print(a.__getitem__(2))
# print(a.__imul__(2))
# print(a.__eq__([1, 2]))
# print(a.__ne__([1,2]))
# print(a.__lt__([10]))
# print(a.__gt__([1]))
# print(a.__ge__([1, 2]))
# print(a.__doc__)
# a.__setitem__(0, 10)
# print(a)
# a.__delitem__(2)
# print(a)

# print(a.__getattribute__('__len__')())

# for i in a.__iter__():
#     print(i)

# print(a.__len__())

# print(list((a.__reversed__())))


# class MyList1(list):
#     def __init__(self, *args):
#         super().__init__(args)
#         print("custom init called")

#     def __new__(cls, *args):
#         print("custom new called")
#         return super().__new__(cls)

# obj = MyList1(1, 2, 3)

# a = [11, 12, 13, 14, 15]
# itr = iter(a)
# print(itr)

# print(next(itr))

# class RemoteControl:
#     def __init__(self, name):
#         self.name = name
#         self.channel = ['BBC', 'DISNEY', 'HBO', 'CNN']
#         self.index = -1
#         self.is_on = False
#         print(f"{self.name} remote is created")

#     def power(self):
#         if self.is_on:
#             print("Remote is turning off")
#             self.is_on = False
#         else:
#             print("Remote is turning on")
#             self.is_on = True
#         return self
    
#     def next_channel(self):
#         if self.is_on:
#             self.index = (self.index + 1) % len(self.channel)
#             print(f"channel changed to : {self.channel[self.index]}")
#         else:
#             print("Remote is off, please turn it on to change the channel")
            
#         return self
        

#     def previous_channel(self):
#         if self.is_on:
#             self.index = (self.index - 1) % len(self.channel)
#             print(f"channel change to : {self.channel[self.index]}")

#         else:
#             print("Remote is off, please turn it on to change the channel")
            
#         return self
    
#     def current_channel(self):
#         if self.is_on:
#             print(f"Current channel is : {self.channel[self.index]}")
#         else:
#             print("Remote is off, please turn it on to see the current channel")

#         return self
    
#     def __str__(self):
#         return f"RemoteControl({self.name})"
    
# if __name__ == "__main__":
#     rc =  RemoteControl("LG")
#     print(rc)
#     rc.power().next_channel().previous_channel()
#     rc.current_channel().power().current_channel()


# class fibonacci():
#     def __init__(self, n):
#         self.n = n 
#         self.a, self.b = 0, 1
#         self.count = 0
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.count < self.n:
#             fib = self.a
#             self.a, self.b = self.b, self.a + self.b
#             self.count += 1
#             return fib
#         else:
#             raise StopIteration

    
# for num in fibonacci(10):
#     print(num)
#     pass

# def remote_control_next():
#     yield "cnn"
#     yield "hbo"
#     yield "disney"

# rc = remote_control_next()
# print(next(rc))
# print(next(rc))
# print(next(rc))
# print(rc)

# for c in rc:
#     print(c)
#     pass

# def fib():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b

# for f in fib():
#     if f > 100:
#         break
#     print(f)
#     pass        

# def square(n):
#     for i in range(n):
#         yield i * i


# for s in square(10):
#     print(s)
#     pass

# LIST COMPREHENSION PROVIDES A WAY TO TRANSFORM A LIST INTO ANOTHER FORMAT
# a = [1, 2, 3, 4, 5]
# b = [i*i for i in a]


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even_numbers = [i for i in numbers if i % 2 == 0]
# squares = [i*i for i in numbers]
# print(even_numbers)
# print(squares)


# cities = ["New York", "Los Angeles", "chicago", "Houston", "Phonenix"]
# countries = ["USA", "INDIA", "UK", "CANADA", "AUS"]
# city_country = zip(cities, countries)
# city_country_dict = {city: country for city, country in city_country}
# print(city_country_dict)


# for a in city_country:
#     print(a)
#     pass

# a = [1, 2, 3, 4, 5, 6]
# b = [4, 5, 6, 7, 8, 9]
# common = [i for i in a if i in b]
# diff = [i for i in a if i not in b]
# diff1 = [i for i in b if i not in a]
# print(common)
# print(diff)
# print(diff1)


#  SET IS UNORDERED AND UNINDEXED
#  SET DOES NOT ALLOW DUPLICATE VALUES
#  SET IS MUTABLE
#  SET CAN STORE DIFFERERNT DATA TYPES
#  SET SUPPORTS MATRHEMATICAL OPERATIONS LIKE UNION, INTERSECTION, DIFFERENCE, SYMMMETRIC DIFFERENCE


# basket = ["apple", "orange", "banana", "kiwi", "grapes", "mango"]
# print(type(basket))

# a = set(basket)
# print(type(a))

# a.add("watermalon")
# a.add("apple")
# a.add("papaya")
# a.add("banana")
# print(a)

# fruits = ["apple", "kiwi", "kiwi"]
# print(fruits)
# print(set(fruits))

# a = set()
# a.add(1)
# a.add(2)
# a.add(3)
# a.add(4)
# a.add(5)
# print(a)
# a.remove(3)
# print(a)

# a = {}
# print(type(a))   an example of dictionary
# b = {1, 2, 3, 0}
# print(type(b))   an example of set


# numbers = [1, 1, 2, 3, 2, 4, 5, 4, 6, 7 ,5 ,4 , 3, 5, 7]
# print("unique numbers: ", set(numbers))

# fs = frozenset(numbers)
# print("frozenset:", fs)

# print(dir(fs))
# a = fs.union({10, 11, 12})
# print(a)

# a = fs.__and__({3, 4})
# a = fs.isdisjoint({10, 11})
# print(a)


x = {"a", "b", "c"}
print("a" in x)
print("d" in x)
y = {"c", "d", "e"}

print(x&y)
print(x|y)

print(x-y)
print(y-x)
print(x^y)
print(y^x)
