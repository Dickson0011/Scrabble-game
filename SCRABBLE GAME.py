# Show game instructions
def show_instructions():
    print("\n Welcome to Scrabble!")
    print("Instructions:")
    print("Enter a word to place on the board.")
    print("Choose a starting row (0-14) and column (0-14).")
    print("Choose a direction: 'across' (→) or 'down' (↓).")
    print("Words must fit on the board.")
    print("Your score is calculated based on letter values.")
    print("Type 'quit' to exit the game.")
    print("Example Input:")
    print("Word: PYTHON")
    print("Row: 7")
    print("Column: 3")
    print("Direction: across")
    print("Have fun playing!\n")

# Call instructions before the game starts
show_instructions()

# Scrabble letter values
letter_values = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1,
    'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
    'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Initialize 15x15 Scrabble board
scrabble_board = [[' ' for _ in range(15)] for _ in range(15)]

# Function to display the board
def display_board(board):
    print("    " + "  ".join(f"{i:2}" for i in range(15)))  # Column numbers
    print("   +" + "---" * 15 + "+")  # Top border
    
    for i, row in enumerate(board):
        print(f"{i:2} | " + " | ".join(row) + " |")  # Row numbers + aligned board
    
    print("   +" + "---" * 15 + "+")  # Bottom border
    print()

# Function to calculate the score of a word
def calculate_score(word):
    return sum(letter_values.get(letter.upper(), 0) for letter in word)

# Function to place a word on the board
def place_word(board, word, row, col, direction):
    print(f"DEBUG: Placing '{word}' at row={row}, col={col}, direction={direction}")
    
    if direction == 'across':
        if all(board[row][col + i] in [' ', word[i]] for i in range(len(word))):
            for i, letter in enumerate(word):
                board[row][col + i] = letter
        else:
            print("Invalid placement: Overlapping letter mismatch.")
            return False
    elif direction == 'down':
        if all(board[row + i][col] in [' ', word[i]] for i in range(len(word))):
            for i, letter in enumerate(word):
                board[row + i][col] = letter
        else:
            print("Invalid placement: Overlapping letter mismatch.")
            return False
    return True

# Main game loop
player_score = 0
while True:
    display_board(scrabble_board)  # Show board before each turn
    
    player_word = input("Enter a word to play (or 'quit' to end the game): ").upper()
    if player_word == 'QUIT':
        break
    
    row = int(input("Enter the starting row (0-14): "))
    col = int(input("Enter the starting column (0-14): "))
    direction = input("Enter the direction ('across' or 'down'): ").lower()

    if direction not in ['across', 'down']:
        print("Invalid direction. Please enter 'across' or 'down'.")
        continue

    # Check if word fits on board
    if (direction == 'across' and col + len(player_word) > 15) or \
       (direction == 'down' and row + len(player_word) > 15):
        print("Word doesn't fit on the board. Try again.")
        continue
    
    # Place word and update score
    if place_word(scrabble_board, player_word, row, col, direction):
        score = calculate_score(player_word)
        player_score += score
        print(f"Score for '{player_word}': {score}")
        print(f"Total Score: {player_score}")
    
    input("Press Enter to continue...")

print("Thanks for playing Scrabble!")
