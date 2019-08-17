import random

def binary_search(search_list, item):

    # Variables to follow the search list
    low = 0
    high = len(search_list) - 1

    i = 1

    # While the algorithm didnt find item position
    while low <= high:

        print("Step: " + str(i))

        # Get central item position
        half = (low + high) // 2
        guess = search_list[half]

        # Check if it is the chosen item
        if guess == item:
            return half

        if guess > item:
            # If guess was to high
            high = half - 1
        else:
            # If guess was to low
            low = half + 1

        i = i + 1

    # item doesnt exist
    return None

my_list = []

# Random
while len(my_list) <= 1000: 
    random_int = random.randint(1,10000)

    if random_int not in my_list:
        my_list.append(random_int)

my_list = sorted(my_list)

print(my_list)
print("\n")

index = random.randint(1, 1000)
item = my_list[index]

print("Item: " + str(my_list[index]) + " at position: " + str(binary_search(my_list, item)))
