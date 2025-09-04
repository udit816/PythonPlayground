import random

START = 1
END = 100

def game_host(target: int, start: int = START, end: int = END) -> None:
    """Human plays by typing guesses; host prints higher/lower feedback."""
    print(f"I'm thinking of a number between {start} and {end}.")
    # print(f"[debug] target = {target}")  # Uncomment while debugging

    while True:
        try:
            guess = int(input(f"Guess a number between {start} and {end}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < start or guess > end:
            print(f"Stay within {start}–{end}.")
            continue

        if guess > target:
            print("Guess is higher.")
        elif guess < target:
            print("Guess is lower.")
        else:
            print("You guessed correctly!")
            break


def guessing_genius(start: int, end: int, target: int) -> int:
    """
    Bot plays optimally using binary search.
    Returns the number of guesses it took.
    """
    low, high = start, end
    steps = 0

    while low <= high:
        # integer midpoint (no float math, no off-by-one)
        guess = low + (high - low) // 2
        steps += 1
        print(f"[step {steps}] range=({low}, {high}) -> guess={guess}")

        if guess == target:
            print(f"Genius found it in {steps} guesses! ✅")
            return steps
        elif guess < target:
            # target is higher → move low up
            low = guess + 1
        else:
            # target is lower → move high down
            high = guess - 1

    # Should never happen if target is within [start, end]
    raise RuntimeError("Target went out of range—check your bounds.")


if __name__ == "__main__":
    # Pick a secret number once
    secret = random.randint(START, END)

    # 1) Let the human play:
    #game_host(secret, START, END)

    # 2) Or let the bot play for you:
    guessing_genius(START, END, secret)
