import numpy as np
import os

class data:

    '''
    Data contains functions used to get the data.
    '''
    
    def __init__(self) -> None:
        
        '''
        This function is used to initialize the variables
        '''

        self.displayMenu()

        while True:
            
            try:
                self.numberOfEntries = int(input("Enter the number of entries: "))
                
                if self.numberOfEntries > 1:
                    break
                else:
                    print("You atleast need 2 entries to plot a graph.")

            except:
                print("Please enter a valid number.")

        self.x = np.empty((self.numberOfEntries) , dtype=float)
        self.y = np.empty((self.numberOfEntries) , dtype=float)

        self.getData()

    def displayMenu(self) -> None:

        '''
        displays the menu
        '''

        os.system('cls')
        print(f"{'='*50}\n{' '*18}Enter the data\n{'='*50}")

    def getData(self) -> None:

        '''
        inputs the data one by one and stores it in the respective array
        '''

        for i in range(self.numberOfEntries):

            self.displayMenu()

            while True:

                try:
                    self.x[i] = float(input(f"Enter the value of x{i+1}: "))
                    print(f"{'='*50}")
                    break
                except:
                    print("Please enter a valid number.")

            while True:

                try:
                    self.y[i] = float(input(f"Enter the value of y{i+1}: "))
                    print(f"{'='*50}")
                    break
                except:
                    print("Please enter a valid number.")

    def getX(self) -> np.ndarray:

        '''
        returns the x array
        '''

        return self.x
    
    def getY(self) -> np.ndarray:

        '''
        returns the y array
        '''

        return self.y