# iterables & Iterators

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {1:0, 2:0, 3:0}
my_range = range(0, 10)

# Iterable?

iterator = iter(my_list)
while True:
    try:
        element = next(iterator)
    except StopIteration:
        break
    print(element)

for i in my_list:
    print(i)

class Counter:
    def __init__(self, count : int):
        self.i = 0
        self.count = count
    

    def __iter__(self):
        return iter(range(self.count))

counter  = Counter(5)
for c in counter:
    print(c)
