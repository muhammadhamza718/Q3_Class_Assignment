# Function to draw a pyramid pattern
def draw_pyramid(rows):
    """
    Ye function ek pyramid print karega jo user ke diye gaye `rows` ka hoga.
    """
    
    # Loop har row ke liye chalega (odd numbers me stars badhenge)
    for i in range(1, rows * 2, 2):  
        # `i` odd numbers me increase hoga -> (1, 3, 5, 7, ...) 
        # Kyunki har row me odd number of stars hote hain.

        # Spaces ka calculation jo pyramid ko center align karega
        spaces = " " * ((rows * 2 - i) // 2)
        # Total available width se current row ke stars ko minus karke uska half spaces banayenge.

        # Stars ka string generate karna (jitne `i` ki value hogi, utne `*` honge)
        stars = "*" * i

        # Final output: spaces + stars + spaces
        print(spaces + stars + spaces)

# User se input lena
try:
    # User se number of rows input lena aur integer me convert karna
    rows = int(input("Enter the number of rows for the pyramid: "))

    # Agar user ne positive number diya hai, to pyramid print karega
    if rows > 0:
        draw_pyramid(rows)
    else:
        # Agar user ne 0 ya negative number diya to warning dega
        print("Please enter a positive integer.")

# Agar user ne koi ghalat input diya (e.g. text ya symbol) to error handle hoga
except ValueError:
    print("Invalid input! Please enter an integer.")

