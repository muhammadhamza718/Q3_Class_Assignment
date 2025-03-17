# Function to draw a diamond pattern
def draw_diamond(rows):
    """
    Ye function ek diamond pattern print karega jo user ke diye gaye `rows` ka hoga.
    """

    # Upper pyramid print karne ke liye loop
    for i in range(1, rows * 2, 2):  
        # `i` odd numbers me increase hoga -> (1, 3, 5, 7, ...) 
        # Kyunki har row me odd number of stars hote hain.

        spaces = " " * ((rows * 2 - i) // 2)  
        # Spaces ka calculation jo pyramid ko center align karega

        stars = "*" * i  
        # Stars ka string generate karna (jitne `i` ki value hogi, utne `*` honge)

        print(spaces + stars + spaces)  
        # Final output: spaces + stars + spaces, taake pyramid centered ho

    # Lower inverted pyramid print karne ke liye loop
    for i in range(rows * 2 - 3, 0, -2):  
        # `i` odd numbers me decrease hoga -> (rows-2, rows-4, ..., 1) 
        # Jo ek inverted pyramid banayega.

        spaces = " " * ((rows * 2 - i) // 2)  
        # Spaces ka calculation taake symmetry bani rahe

        stars = "*" * i  
        # Stars ka string generate karna (jitne `i` ki value hogi, utne `*` honge)

        print(spaces + stars + spaces)  
        # Final output: spaces + stars + spaces

# User se input lena
try:
    rows = int(input("Enter the number of rows for the diamond: "))  
    # User se number of rows input lena aur integer me convert karna

    if rows > 0:
        draw_diamond(rows)  
        # Agar input valid hai to function call karega
    else:
        print("Please enter a positive integer.")  
        # Agar user ne 0 ya negative number diya to warning dega

except ValueError:
    print("Invalid input! Please enter an integer.")  
    # Agar user ne koi ghalat input diya (e.g. text ya symbol) to error handle hoga
