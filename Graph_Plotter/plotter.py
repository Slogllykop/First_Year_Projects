import os
import time
import numpy as np
import matplotlib.pyplot as plt

class graph:

    '''
    Class contains the functions to plot the graph.
    '''

    def __init__(self, x, y) -> None:

        '''
        This function is used to initialize the variables.
        '''

        self.x = x
        self.y = y

        self.name = ''
        self.rollNumber = 0
        self.xAxisName = ''
        self.yAxisName = ''
        self.title = ''

        self.setDetails()
    
    def displayMenu(self) -> None:

        '''
        displays the menu
        '''

        os.system('cls')
        print(f"{'='*50}\n{' '*18}Enter the data\n{'='*50}")

    def plot(self) -> None:

        '''
        plot function is used to plot the graph.
        '''

        # returns coefficients of the polynomial of degree n that is a best fit to the data points (x, y)
        coeff = np.polyfit(self.x, self.y, 1)
        # equation of the line = y = mx + c where m is the slope and c is the y-intercept
        yLine = coeff[1] + coeff[0] * self.x

        f, mainCanvas=plt.subplots(figsize = (10, 5))
        mainCanvas.grid()
        mainCanvas.plot(self.x, yLine, marker='o', markerfacecolor='red', label ="Best fit")

        plt.scatter(self.x, self.y, label ="Data points")
        # plt.plot(self.x, yLine, 'r')
        plt.title(self.title)
        plt.xlabel(self.xAxisName)
        plt.ylabel(self.yAxisName)
        plt.legend(bbox_to_anchor =(1.07, 1.15), ncol = 2)
        plt.text(-0.05, 1.1, f'Roll no: {self.rollNumber} - {self.name}', horizontalalignment='left', verticalalignment='center', transform=mainCanvas.transAxes)
        
        os.system('cls')
        print(f"{'='*50}\n{' '*18}Graph Plotter\n{'='*50}")

        for i in range(5):

            for i in "|/-\\":

                print(f"Processing graph for {self.name}...{i}",end='\r')
                time.sleep(0.2)

        else:

            os.system('cls')
            print(f"{'='*50}\n{' '*18}Graph Plotter\n{'='*50}")
            print(f"{' '*11}Graph plotted successfully.\n{'='*50}")
            plt.show()

    
    def setDetails(self) -> None:
        
        '''
        setDetails function is used to set the details of the graph.
        '''

        self.displayMenu()
        while True:
            
            self.title = input("Enter the title of the graph: ")

            if self.title != '':
                break
            else:
                print("Title cannot be empty.")
        
        self.displayMenu()
        while True:

            self.xAxisName = input("Enter the name of x axis: ")

            if self.xAxisName != '':
                break
            else:
                print("x axis name cannot be empty.")
        
        self.displayMenu()
        while True:

            self.yAxisName = input("Enter the name of y axis: ")

            if self.yAxisName != '':
                break
            else:
                print("y axis name cannot be empty.")
        
        self.displayMenu()
        while True:

            self.name = input("Enter your name: ")

            if self.name != '':
                break
            else:
                print("Name cannot be empty.")

        self.displayMenu()
        while True:
            
            try:
                self.rollNumber = int(input("Enter your roll number: "))
                break
            except:
                print("Please enter a valid number.")