# -------------------------------------------------------------------------------
# Ken_Lee_Project_DRIVER.py
# Name: Ken Lee
# Python Version: 3.6.4
# -------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
# -------------------------------------------------------------------------------
# References: 
# -------------------------------------------------------------------------------
# Comments to grader: 
# -------------------------------------------------------------------------------
# Code: Code starts here
# -------------------------------------------------------------------------------


from Ken_Lee_Project_GUI import TheGUI
from tkinter import *


# Starts up the game
def main():
    root = Tk()
    root.title("KenKen by Ken Lee")
    root.geometry("600x660")
    TheGUI(root)
    root.mainloop()


main()
