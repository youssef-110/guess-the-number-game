"""Guess the number from 1 to 1000. The game says higher or lower until you get it."""

import random

LOW, HIGH = 1, 1000


def hint(secret: int, guess: int) -> str:
    if guess < secret:
        return "higher"
    if guess > secret:
        return "lower"
    return "correct"


def main() -> None:
    secret = random.randint(LOW, HIGH)
    print(f"I picked a number from {LOW} to {HIGH}. Guess it.")
    tries = 0
    while True:
        raw = input("> ").strip()
        if not raw.isdigit() or not LOW <= int(raw) <= HIGH:
            print(f"Type a whole number from {LOW} to {HIGH}.")
            continue
        tries += 1
        result = hint(secret, int(raw))
        if result == "correct":
            print(f"Winner winner chicken dinner! {secret} in {tries} tries.")
            return
        print(f"Go {result}.")


if __name__ == "__main__":
    main()
