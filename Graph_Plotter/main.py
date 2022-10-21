from plotter import graph
from data import data
import os

if __name__ == '__main__':

    flag = True
    while flag:

        dimensions = 'mode 50'
        color = 'color 0F'
        os.system(dimensions)
        os.system(color)

        D = data()
        xPoints = D.getX()
        yPoints = D.getY()

        p = graph(xPoints , yPoints)
        p.plot()

        while True:

            choice = (input("Do you want to plot another graph? (y/n): "))

            if choice == 'n' or choice == 'N':
                flag = False
                final = input("\nPress Enter to exit...")
                break

            elif choice == 'y' or choice == 'Y':
                break

            else:
                print("Please choose a valid option.")