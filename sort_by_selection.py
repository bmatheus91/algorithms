import random

# Find the smaller value in the array


def smaller_search(arr):
    # Store array's smaller value and index
    smaller = arr[0]
    smaller_index = 0

    # Loop through array to find the smaller value
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smaller_index = i

    return smaller_index


def order_by_selection(arr: list):
    new_arr = []

    for i in range(len(arr)):
        # Search for the smaller index in the array
        smaller = smaller_search(arr)

        # Remove the smaller value from old array and append it to the new one
        new_arr.append(arr.pop(smaller))

    return new_arr


my_list = []

# Random
while len(my_list) <= 50:
    random_int = random.randint(1, 100)

    if random_int not in my_list:
        my_list.append(random_int)

print(my_list)
print("\n")

print(order_by_selection(my_list))
