def sum_numbers(a, b):
    result = a + b
    print(f"The sum of two numbers {a} and {b} is: {result}")

# sum_numbers(5, 10)


name = "Alice"
def greet_user(name):
    print(f"Hello, {name}! Welcome to our application.")
    pass
    
# greet_user("Bob")

def get_user():
    global name
    name = "Charlie"
    print(f"Fetching user name {name}")
    
# get_user()


def calculate_area(length, width):
    area = length * width
    if area > 50 and area < 200:
        print("Large area")
    elif area != 50:
        print("Small area")
    elif area ==100 or area ==150:
        print("Medium area")
    elif area <= 50:
        print("Tiny area")
    print(f"The area of the rectangle with length {length} and width {width} is: {area}")
    
# calculate_area(1, 50)

def display_message(message="Hello, World!"):
    message_data = {
        "sender":"Admin",
        "content": message,
        "timestamp":"2024-06-01 10:00:00",
        "recepient":"User"
    }
    print(f"Sender: dict.get()") 

# loops
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        
# print_numbers()

# lists comprehension
def square_numbers(numbers):
    squared = [x**2 for x in numbers]
    print(f"Squared numbers: {squared}")

square_numbers([1, 2, 3, 4, 5])

#generator expression
def generate_squares(n):
    squares = (x**2 for x in range(1, n+1))
    for square in squares:
        print(f"Square: {square}")
        
generate_squares(5)