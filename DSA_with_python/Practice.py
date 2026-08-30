
# #  QUES 1

weather = {}
with open('jan_day.txt', 'r') as f:
    for line in f:
        tokens = line.strip().split(',')
        day = tokens[0].strip()
        temp = int(tokens[1].strip())
        weather[day] = temp
print(weather)
print(weather['Jan 9'])      
print(weather['Jan 4'])

# #  QUES 2

list = []
with open('jan_day.txt', 'r') as f:
    for line in f:
        tokens = line.split(',')
        
        temp = int(tokens[1])
        list.append(temp)
print(list)

avg = sum(list[0:7])/len(list[0:7])
print(max(list[0:10]))
print(avg)

# #  QUES 3

w = {}
with open('poem.txt', 'r') as f:
    for line in f:
        words = line.split(' ')
        for word in words:
          word = word.replace('\n','')
          w[word] = len(word)   

 
print(w)

# #  QUES 4

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def get_prob_range(self, index):
        return[*range(index, len(self.arr))] + [*range(0, index)]
    
    def get_item(self, key):
        h = self.get_hash(key)
        if self.get_hash[h] is None:
            return 
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element[0] is None:
                return
            if element[0] == key:
                return element[1]
            
    def set_item(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)

        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("hashmap full")

    def del_item(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return
            if self.arr[prob_index] == key:
               self.arr[prob_index] = None

        print(self.arr)


t = HashTable
print(t.arr)



def prime_square_nth(n):
    MAX = 1300000  # Large enough to find first 100000 primes
    is_prime = [True] * MAX
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes
    for i in range(2, int(MAX ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX, i):
                is_prime[j] = False

    # Collect primes until we reach the N-th one
    count = 0
    for i in range(2, MAX):
        if is_prime[i]:
            count += 1
            if count == n:
                return i * i

# Read input and print output
n = int(input())
print(prime_square_nth(n))
