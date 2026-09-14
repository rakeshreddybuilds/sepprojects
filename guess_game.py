# secret_number = 22
# guess_count = 0
# guess_limit = 3

# while guess_count < guess_limit:
#   guess = int(input("Gues the number you idiot: "))
#   guess_count += 1
#   if guess == secret_number:
#     print("YOU Won idiot!")
#     break
# else:
#     print("YOU Lost idiot!")


command = ""


while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car Started......")
    elif command == "stop":
        print("Car Stopped......")
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit the game
        """)
    elif command == "quit":
        print("Quitting the game...")
  
else:
    print("Sorry I don't understand that!")