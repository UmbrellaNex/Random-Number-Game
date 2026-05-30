import random

for _ in range(100):

    print("WELCOME TO THE RANDOM NUMBER GAME".center(50))
    print("TOTAL 8 CHANCES TO GUESS\n".center(50))

    RandomNumber = random.randint(1, 100)

    try:

        for Guesses in range(8):

            UserGuesses = int(input("Enter Your Guess : "))

            if UserGuesses == RandomNumber:

                print(f"\n*** YOU WIN ***")
                print(f"You Guessed the Number in {Guesses + 1} Attempts")

                # HIGH SCORE ONLY ON WIN
                try:
                    with open("highscore.txt", "r") as f:
                        HighScore = int(f.read())

                except:
                    HighScore = None

                # CREATE OR UPDATE HIGH SCORE
                if HighScore is None or (Guesses + 1 < HighScore):

                    with open("highscore.txt", "w") as f:
                        f.write(str(Guesses + 1))

                    print("NEW HIGH SCORE SAVED!")

                else:
                    print(f"CURRENT HIGH SCORE : {HighScore}")

                break

            elif UserGuesses > RandomNumber:

                print("Please Enter a Smaller Number\n")

            else:

                print("Please Enter a Larger Number\n")

        else:

            print("\n*** YOU LOSE ***")
            print(f"The Correct Number Was : {RandomNumber}\n")

        PlayAgain = input("Do You Want to Play Again? (Yes/No) : ").lower()

        if PlayAgain != "yes":

            print("\nThank You For Playing")
            break

    except ValueError:

        print("\nPlease Enter a Valid Number!\n")
