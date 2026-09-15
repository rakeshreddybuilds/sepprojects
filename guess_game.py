import random


def main():
  secret = random.randint(1, 100)
  attempts = 0
  max_attempts = 8


  print("Guess the number that i am thinking??")
  print(f"you have{max_attempts} attempts to guess it.\n")


  while attempts < max_attempts:
    guess_input = input("Your guess: ").strip()


    if not guess_input.isdigit():
      print("Please enter a valid number.\n")
      continue

    guess = int(guess_input)
    attempts += 1

    if guess < 1 or guess > 100:
      print("Enter a number between 1 and 100.\n")
    elif guess < secret:
      print("Too low\n")
    elif guess > secret:
      print("Too high!\n")
    else:
      print(f"Correct! You guessed it in {attempts} attempts.")
      break

    remaining = max_attempts - attempts
    if remaining > 0:
      print(f"Attempts left: {remaining}\n")
  else:
    print(f"\nOut of attempts! The number was {secret}.")


  play_again = input("\nPlay again? (y/n): ").strip().lower()
  if play_again == "y":
    main()
  else:
    print("Thanks for playing!")


if __name__ == "__main__":
  main()
