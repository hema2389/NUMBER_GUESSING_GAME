import random
game=True
while game:
  number = random.randint(1,100)
  attempts=0
  print("New Game Started!!. Guess number to continue or type 'exit'")

  while game:
    guess = input("Enter a guess: ")
    if guess=="exit":
      print("Nice playing with you! Comeback to play again!")
      game=False
      break
    try:
      guess=int(guess)
      attempts += 1
      if guess > number:
        print("Too high.. Guess a little low")
      elif guess < number:
        print("Too low.. Guess a little high")
      else:
        print("Hurray!!! You found the Number ", number, "in ", attempts, "attempts")
        break
    except ValueError:
      print("Guess an integer")
