def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display = "".join(ch if ch in guesses else "_" for ch in secret_word)
        print(display)
        return all(ch in guesses for ch in secret_word)
    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter the secret word: ").strip().lower()
    game = make_hangman(secret)
    while True:
        letter = input("Guess a letter: ").strip().lower()
        done = game(letter)
        if done:
            print("You won!")
            break