import random  # Import random module for generating random numbers

# Welcome message
print("🎲 Welcome to the Number Guessing Game!")
print("Type 'quit' or 'exit' to stop the game\n")

# Keep playing until user wants to stop
while True:
    # Generate a random secret number between 1 and 10 for each round
    secret_number = random.randint(1, 10)
    attempt = 0
    
    print("--- New Round! ---")
    
    # Start guessing loop for this round
    while True:
        # Get user input
        user_input = input("Enter a number between 1 and 10 (or type 'quit' to exit): ")
        
        # Check if user wants to quit
        if user_input.lower() == 'quit' or user_input.lower() == 'exit':
            print("👋 Thanks for playing! Goodbye!")
            exit()  # Stop the entire program
        
        # Convert to integer for guessing
        guess = int(user_input)
        attempt += 1
        
        # Check the guess
        if guess == secret_number:
            print(f"🎉 Correct! You guessed the number in {attempt} tries!\n")
            break  # End this round, start a new one
        elif guess > secret_number:
            print("⬆ Too high! Try again")
        else:
            print("⬇ Too low! Try again")