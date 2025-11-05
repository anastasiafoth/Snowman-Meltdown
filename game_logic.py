import random
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

from ascii_art import STAGES

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Checks if guessed letter is correct and displays the stages of the snowman"""
    displayed_word_list = []

    for char in secret_word:
        if char in guessed_letters:
            displayed_word_list.append(char)
        else:
            displayed_word_list.append("_ ")
    displayed_word = " ".join(displayed_word_list)
    print(STAGES[mistakes])
    print(f"Word: {displayed_word}\n")
    return displayed_word


def play_game():
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    print("=" * 36)
    print("    Welcome to Snowman Meltdown!")
    print("=" * 36, end="")
    print("""
*         *        .     *     .
*     .     *       *      *
      """, end="")
    while mistakes < 6:
        displayed_word = display_game_state(mistakes, secret_word, guessed_letters)
        if displayed_word.replace(" ", "") == secret_word:
            print("Congratulations, you saved the snowman!")
            break

        while True:
            guess = input("Guess a letter: ").lower()
            special_chars = [
                "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
                "-", "_", "=", "+", "[", "]", "{", "}", ";", ":",
                "'", '"', "\\", "|", ",", ".", "<", ">", "/", "?",
                "`", "~", "§", "´"
            ]
            if guess.isdigit() or guess in special_chars:
                print("The letter shouldn´t contain digits or special characters.")
            elif len(guess) == 1:
                guessed_letters.append(guess)
                break
            else:
                print("Please enter one letter only.")

        if guess not in secret_word:
            mistakes += 1
            if mistakes == 6:
                print(STAGES[-1])
                print(f"Game Over! The word was: {secret_word}")
