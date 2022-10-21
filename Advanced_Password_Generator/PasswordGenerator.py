import os
import random as r
import string_utils as su


class Generator:

    '''
    Class contaning functions to generate passwords.
    '''

    def clear(self) -> None:
        
        '''
        clear function is used to clear the screen so that new UI can be printed.
        '''
        
        os.system('cls')

    def __init__(self) -> None:

        '''
        init function is used to initialize the variables.
        '''

        self.clear()

        self.lowercase = "abcdefghijklmnopqrstuvwxyz"
        self.uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.digits = "0123456789"
        self.special = "!@#$%^&*()-_=+[{]}|;:,<.>/?`~"

        print(f"{'='*50}\n{' '*16}Password Generator\n{'='*50}")

        self.no_of_password = 1
        self.lower = 0
        self.upper = 0
        self.numbers = 0
        self.symbols = 0

        self.characterChoices = [0 for x in range(4)]

        self.length = 0
        self.getLength()
        self.available = self.length
        self.getNoOfPassword()
        self.password = ['' for x in range(self.no_of_password)]
        self.run()

    def getNoOfPassword(self) -> None:

        '''
        This function is used to get the number of passwords to be generated.
        '''

        while True:

            try:

                self.no_of_password = int(input("How many passwords do you want to generate: "))
                
                if self.no_of_password < 1:
                    print("Number of passwords cannot be less than 1!")

                else:
                    print(f"{'='*50}")
                    break

            except:
                print("Enter a valid number!")

    def getLength(self) -> None:

        '''
        get_length function is used to get the length of the password.
        '''

        while True:

            try:
                self.length = int(input("Enter the length of the password: "))
                if self.length < 8:
                    print("Password length cannot be less than 8!")
                else:
                    print(f"{'='*50}")
                    break
            except:
                print("Enter a valid number!")
    
    def getLower(self) -> None:

        '''
        getLower function is used to get the number of lowercase letters.
        '''

        while True:
            if self.available != 0 :
                try:
                    lower = int(input("Enter the number of lowercase letters: "))

                    if lower < 0:
                        print("Number can't be less than 0!")

                    elif lower > self.available:
                        print("Number can't be greater than available characters!")

                    elif lower > self.length:
                        print("Number can't be greater than the actual length!")

                    else:
                        self.lower = lower
                        self.available -= self.lower
                        self.characterChoices[0] = self.lower
                        break
                except:
                    print("Enter a valid number!")
            else:
                print("No more characters available!")
                break
    
    def getUpper(self) -> None:

        '''
        getUpper function is used to get the number of uppercase letters.
        '''

        while True:
            if self.available != 0 :
                try:
                    upper = int(input("Enter the number of uppercase letters: "))

                    if upper < 0:
                        print("Number can't be less than 0!")

                    elif upper > self.available:
                        print("Number can't be greater than available characters!")

                    elif upper > self.length:
                        print("Number can't be greater than the actual length!")

                    else:
                        self.upper = upper
                        self.available -= self.upper
                        self.characterChoices[1] = self.upper
                        break
                except:
                    print("Enter a valid number!")
            else:
                print("No more characters available!")
                break

    def getNumbers(self) -> None:

        '''
        getNumbers function is used to get the number of digits.
        '''

        while True:
            if self.available != 0 :
                try:
                    numbers = int(input("Enter the number of numbers: "))

                    if numbers < 0:
                        print("Number can't be less than 0!")

                    elif numbers > self.available:
                        print("Number can't be greater than available characters!")

                    elif numbers > self.length:
                        print("Number can't be greater than the actual length!")

                    else:
                        self.numbers = numbers
                        self.available -= self.numbers
                        self.characterChoices[2] = self.numbers
                        break
                except:
                    print("Enter a valid number!")
            else:
                print("No more characters available!")
                break
    
    def getSymbols(self) -> None:
        
        '''
        getSymbols function is used to get the number of symbols.
        '''

        while True:
            if self.available != 0 :
                try:
                    symbols = int(input("Enter the number of symbols: "))

                    if symbols < 0:
                        print("Number can't be less than 0!")

                    elif symbols > self.available:
                        print("Number can't be greater than available characters!")

                    elif symbols > self.length:
                        print("Number can't be greater than the actual length!")

                    else:
                        self.symbols = symbols
                        self.available -= self.symbols
                        self.characterChoices[3] = self.symbols
                        break
                except:
                    print("Enter a valid number!")
            else:
                print("No more characters available!")
                break
        
    def displayChoices(self, available_choices) -> None:

        '''
        Displays the available choices to the user and returns the choice.
        '''

        database = []

        if len(available_choices) != 0:
            
            self.clear()

            print(f"\n{'='*50}\n{' '*16}Password Generator\n{'='*50}")

            print(f"Characters available: {self.available}\n{'='*50}")

            print(f"{' '*14}-:Available choices:-")

            for i in range(len(available_choices)):

                choices = 'Lower case' if available_choices[i] == self.getLower else 'Upper case' if available_choices[i] == self.getUpper else 'Numbers' if available_choices[i] == self.getNumbers else 'Symbols' if available_choices[i] == self.getSymbols else None
                
                database.append([i,choices])

                print(f"{i+1}] {choices}")
                
            else:

                print(f"{'='*50}")

                while True:

                    try:

                        choices_length = len(available_choices)

                        current_choice = int(input("Enter your choice: "))

                        if current_choice < 1 or current_choice > choices_length:
                            print("Enter a valid choice!")

                        else:
                            self.current_choice = database[current_choice-1][1]
                            break

                    except:
                        print("Enter a valid choice!")

    def display(self) -> None:

        '''
        displays the UI of the application.
        '''

        self.clear()

        print(f"\n{'='*50}\n{' '*16}Password Generator\n{'='*50}")

        print(f"Characters available: {self.available}\n{'='*50}")

        available_choices = [self.getLower, self.getUpper, self.getNumbers, self.getSymbols]

        while self.available != 0:

            self.displayChoices(available_choices)

            match self.current_choice:

                case 'Lower case':
                    available_choices.remove(self.getLower)
                    self.getLower()

                case 'Upper case':
                    available_choices.remove(self.getUpper)
                    self.getUpper()

                case 'Numbers':
                    available_choices.remove(self.getNumbers)
                    self.getNumbers()

                case 'Symbols':
                    available_choices.remove(self.getSymbols)
                    self.getSymbols()

    def run(self) -> None:
        
        '''
        run function is used to run the application.
        '''

        self.display()

        self.clear()

        print(f"\n{'='*50}\n{' '*16}Password Generator\n{'='*50}")

        print(f"{' '*13}-:Generated Passwords:-\n{'='*50}")

        for ps in range(self.no_of_password):

            single_password = ""
            for i in range(len(self.characterChoices)):

                if self.characterChoices[i] != 0:

                    if i == 0:

                        for j in range(self.characterChoices[i]):

                            single_password += r.choice(self.lowercase)

                    elif i == 1:

                        for j in range(self.characterChoices[i]):

                            single_password += r.choice(self.uppercase)

                    elif i == 2:

                        for j in range(self.characterChoices[i]):

                            single_password += r.choice(self.digits)

                    elif i == 3:

                        for j in range(self.characterChoices[i]):

                            single_password += r.choice(self.special)

            else:

                self.password[ps] = su.shuffle(single_password)
                single_password = ""
        else:

            for i in self.password:
                print(i)

            else:

                print(f"{'='*50}")
                isFile = input("Do you want to save it in a text file (y/n): ")

                if isFile == 'y' or isFile == 'Y':

                    with open("passwords.txt" , 'w' , encoding = 'utf-8') as f:

                        for i in self.password:
                            f.write(i + '\n')

                    print(f"{'='*50}\n{' '*7}Successfully saved as passwords.txt\n{'='*50}")
                
                else:

                    print(f"{'='*50}")
                
                runAgain = input("Do you want to generate again? (y/n): ")
        
                if runAgain == 'y' or runAgain == 'Y':
                
                    self.__init__()
                    self.run()
        
                else:
                
                    input("\nPress Enter to exit...")
                    self.clear()
                    exit()