import random

# Function to generate a random 3-digit secret number
def generate_secret_number():
    """
    Ye function ek random 3-digit number generate karega 
    jisme har digit unique ho sakti hai.
    """
    return str(random.randint(100, 999))  # 100 se 999 tak koi bhi number choose karega

# Function to check the player's guess and provide feedback
def check_guess(secret, guess):
    """
    Ye function user ke guess ko secret number se compare karega 
    aur feedback return karega:
    👌 (Correct): Agar digit sahi position pe hai
    👍 (Ok): Agar digit hai lekin galat position pe hai
    ❌ (Wrong): Agar digit bilkul bhi nahi hai
    """
    feedback = []

    for i in range(3):  # Kyunki 3-digit number hai
        if guess[i] == secret[i]:  
            feedback.append("👌")  # Agar digit aur position dono sahi hain
        elif guess[i] in secret:  
            feedback.append("👍")  # Agar digit hai lekin position galat hai
        else:
            feedback.append("❌")  # Agar digit hi nahi mil rahi

    return " ".join(feedback)  # Feedback ko ek string me convert karke return karega

# Main game function
def play_game():
    """
    Ye function pura game control karega, secret number generate karega, 
    user se guesses lega aur feedback dega.
    """
    secret_number = generate_secret_number()  # Random secret number generate karna
    attempts = 10  # User ke pass 10 chances hain

    # Game Rules Print Karna
    print("🎮 Welcome to the Guessing Game! 🎮\n")
    print("Game Rules:")
    print("1️⃣ You need to guess a secret 3-digit number.")
    print("2️⃣ After each attempt, you will get hints:")
    print("   - 👌 (Correct) → If the digit and its position are both correct.")
    print("   - 👍 (Ok) → If the digit exists but is in the wrong position.")
    print("   - ❌ (Wrong) → If the digit is not in the number at all.")
    print("3️⃣ You have a total of 10 attempts.")
    print("4️⃣ If you don't guess correctly within 10 attempts, the game is over.\n")
    print("Let's begin!\n")

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}/{attempts}: Enter your 3-digit guess: ")

        # Input validation: Check karega ke guess 3-digit ka integer hai
        if not guess.isdigit() or len(guess) != 3:
            print("❌ Invalid input! Please enter a 3-digit number.\n")
            continue

        # Check karega ke user ka guess sahi hai ya nahi
        feedback = check_guess(secret_number, guess)

        print(feedback + "\n")  # Feedback print karega

        if feedback == "👌 👌 👌":  # Agar teeno digits aur position sahi hain
            print("🎉 Congratulations! You guessed the correct number!\n")
            break
    else:
        # Agar user 10 guesses me sahi answer nahi de saka
        print(f"🚨 Game Over! The correct number was {secret_number}.\n")

# Run the game
play_game()
