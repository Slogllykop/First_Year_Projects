import os
import random as r

class Game:

    '''
    Game class is used to play the game.
    '''

    def __init__(self) -> None:

        '''
        init function is used to initialize the game and all the variables.
        '''

        self.clear()

        print(f"{'='*50}\n{' '*17}Guess the number{' '*17}\n{'='*50}")

        while True:

            try:

                self.start, self.stop = map(int, input("Enter the range [eg. 0-100]: ").split("-"))

                if self.stop - self.start < 75:

                    print("Minimum range can't be less than 75!")

                else:

                    if self.start < 0:

                        print("Start of the range can't be negative!")

                    else:

                        if self.stop < 75:
                            
                            print("Stop of the range can't be less than 75!")

                        else:
                            break

            except:
                print("Enter a valid range!")

        self.chances = 0
        self.number = r.randint(self.start, self.stop)
        self.previous = []
        self.msg = ""

        print(f"{'='*50}\n{' '*10}-:Enter the difficulty level:-\n1] Easy (13 chances)\n2] Medium (10 chances)\n3] Hard (5 chances)\n4] Impossible (3 chances)\n{'*'*50}")
        
        while True:

            try:

                level = int(input("Enter your index: "))

                if level != 0:

                    match level:
                    
                        case 1:
                            self.chances = 13
                            print(f"{'*'*50}")
                            break
                    
                        case 2:
                            self.chances = 10
                            print(f"{'*'*50}")
                            break
                    
                        case 3:
                            self.chances = 5
                            print(f"{'*'*50}")
                            break

                        case 4:
                            self.chances = 3
                            print(f"{'*'*50}")
                            break

                        case _:
                            print("Enter a valid number!")

                else:
                        print("Enter a valid number!")

            except:
                print("Enter a valid number!")

    def clear(self) -> None:

        '''
        clear function is used to clear the screen so that new UI can be printed.
        '''

        os.system('cls')

    def display(self) -> None:

        '''
        display function is used to display the UI.
        '''

        self.clear()

        print(f"\n{'='*50}\n{' '*17}Guess the number{' '*17}\n{'='*50}")

        print(f"Previously made Choices for range ({self.start}-{self.stop}):- ")

        for i in range(len(self.previous)):

            if i != len(self.previous) - 1:
                print(f"{self.previous[i]}, ", end="")

            else:
                print(f"{self.previous[i]}", end="")

        print(f"\n{'='*50}\nChances left: {self.chances}\n{'='*50}")
        print(f"{self.msg}\n{'='*50}")

    def run(self):

        '''
        run function is used to run game.
        '''

        self.flag = True

        while self.flag:

            while True:

                try:
                    self.guess = int(input("Guess a number: "))
                    break

                except:
                    print("Enter a valid number!")

            if self.guess < self.start or self.guess > self.stop:

                self.msg = f"Number should be in range ({self.start}-{self.stop})!"

            elif self.guess == self.number:

                print(f"The number was indeed: {self.number}\n{'='*50}\n{' '*21}You won!\n{'='*50}")
                self.choice = input("Do you want to play again? [y/n]: ")

                if self.choice == "y" or self.choice == "Y":
                    self.__init__()
                    self.run()

                else:
                    self.chances = 0
                    input("\nPress Enter to exit...")
                    self.flag = False

            elif self.guess < self.number:

                if self.guess in self.previous:

                    self.msg = f"You have already entered this number!\n{'='*50}\n{' '*15}Guess a higher number"
                    self.previous.remove(self.guess)
                    self.chances += 1

                else:
                    self.msg = f"{' '*15}Guess a higher number"

            elif self.guess > self.number:

                if self.guess in self.previous:

                    self.msg = f"You have already entered this number!\n{'='*50}\n{' '*15}Guess a lower number"
                    self.previous.remove(self.guess)
                    self.chances += 1

                else:
                    self.msg = f"{' '*15}Guess a lower number"

            if self.guess < self.start or self.guess > self.stop:
                pass

            else:
                self.previous.append(self.guess)
                self.chances -= 1

            self.display()

            if self.chances == 0:

                print(f"The number was: {self.number}\n{'='*50}\n{' '*20}You lost!\n{'='*50}")
                self.choice = input("Do you want to play again? [y/n]: ")

                if self.choice == "y" or self.choice == "Y":
                    self.__init__()
                    self.run()

                else:
                    input("\nPress Enter to exit...")
                    self.flag = False