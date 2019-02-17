from firstname_lastname_Project_CLASS import KenKen
from tkinter import *
from tkinter import messagebox


class TheGUI(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.kenken = KenKen()

        # This keeps track of the puzzle number
        self.counter: int = 0
        self.puzzles = self.kenken.getpuzzles()
        self.linelist = self.kenken.getlines()

        self.choice = ['', '1', '2', '3', '4', '5']
        self.surrender_list = []  # List unique to surrend method to hold all relevant numbers

        # Buttons for the puzzle
        self.lblPuz = StringVar(self)
        self.lblPuz.set("Puzzle " + str(self.counter + 1))
        self.lbl1 = Label(self, textvariable=self.lblPuz,
                          font="Arial 20 bold").pack()

        self.good_luck = Label(self, text='GOOD LUCK!', font='Arial 10 bold').pack()
        self.win = Button(self, text='WIN?', command=self.check).pack(side=TOP, fill=X)
        self.next_puzzle = Button(self, text='Next Puzzle', command=self.next).pack(fill=X)

        self.reset_button = Button(self, text='RESET', command=self.reset).pack(side=LEFT)
        self.exit_button = Button(self, text='EXIT', command=self.exit).pack(side=RIGHT, fill=X)
        self.surrender = Button(self, text='Surrender?',
                                command=self.surrend).pack(side=BOTTOM, fill=X, expand=YES)

        # Put all the buttons into a list
        self.buttonlist = [self.win, self.next_puzzle, self.reset_button, self.exit_button, self.surrender]

        self.solution = self.kenken.surrender(self.counter)

        # Creating the components on the GUI
        self.w = Canvas(master, width=502, height=503)
        self.w.pack()

        self.tt = StringVar(self)
        self.sqlist = []
        # This keeps track of the values for each block
        self.movelist = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.numbers = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        # Creates the puzzle depending on the counter
        self.create_widgets()
        self.w.bind("<ButtonRelease-1>", self.change)
        self.pack()

    def create_widgets(self):
        # Creates the border and grid for the GUI
        self.w.create_rectangle(5, 5, 500, 500, width=4)
        # iterates through a pixel space of 500, making a line every 100th pixel
        for i in range(0, 500, 100):  # Creates the grid
            for j in range(0, 500, 100):
                x = j + 100
                y = i + 100
                self.squares = self.w.create_rectangle(j, i, x, y)

        # While loop to set the KenKen lines
        # self.linelist grabs the getlines method from the class file
        # self.counter iterates through the lines list depending on which puzzle the user is on
        # list_index iterates through every object within the specified list within the lines list
        # the [0],[1],[2],[3] is because create_line requires a x0,x1,y0,y1
        # ---- also because there are 12 elements within each list, having more than 4 causes index errors
        list_index: int = 0
        while list_index <= 12:
            a = self.linelist[self.counter][list_index][0]
            b = self.linelist[self.counter][list_index][1]
            c = self.linelist[self.counter][list_index][2]
            d = self.linelist[self.counter][list_index][3]

            list_index += 1
            # This creates the actual inner lines them self
            self.w.create_line(a, b, c, d, width=4)

        # Obtains the specified list from self.puzzlelist in class
        # items gathers all the indexes in the list
        # self.counter keeps track of which puzzle it is
        for items in range(len(self.puzzles)):
            self.current_puzzle = self.puzzles[items][self.counter]

        # This outputs everything inside self.current_puzzle into each square
        # The start position for x sets the x axis start at 25 pixels
        # The start position for y sets the y axis to start at 20 pixels
        # puzzle_index used as an iterator for self.current_puzzle, outputs ea. element in ea. square
        puzzle_index: int = 0
        for x in range(25, 500, 100):
            for y in range(20, 500, 100):
                self.w.create_text(x, y, font="Calibri 16 bold",
                                   text=self.current_puzzle[puzzle_index])
                puzzle_index += 1

        x = 0
        for i in range(50, 500, 100):
            y = 0
            for j in range(50, 500, 100):
                self.numbers[x][y] = self.w.create_text(i, j, font=("Calibri 24 bold"), text=self.choice[0])
                a = self.numbers
                y += 1
            x += 1

    def exit(self):
        # Method that exits the GUI when the Exit button is pressed
        exit()

    def check(self):
        # Checks to see if the user wins
        self.check = self.kenken.checkit(self.movelist, self.counter)
        if self.movelist == self.check:
            messagebox.showinfo('Congratulations','You won the game!')

    def change(self, event):
        # Updates the buttons to the current number
        row, column = self.kenken.changer(event)
        self.movelist[row][column] += 1

        if self.movelist[row][column] > 5:
            self.movelist[row][column] = 0

        self.w.itemconfigure(self.numbers[row][column],
                             text=self.choice[self.movelist[row][column]])
        # As the user plays, it will continually check if the user wins or not
        self.check()

    def resetnums(self):
        # Resets all the current numbers
        self.movelist = self.kenken.resetnum(self.movelist)

    def reset(self):
        # Recreate the same game
        self.w.delete('all')
        self.resetnums()
        self.buttonlist.append(self.lbl1)
        self.create_widgets()

        '''for i in range(len(self.buttonlist)):
            self.buttonlist[i].destroy()'''

    def surrend(self):
        # Shows the solution
        self.reset()
        for items in self.solution:
            self.surrender_list.append(items)
        surrender_list1 = []

        for i in range(5):
            for j in range(5):
                surrender_list1.append(self.surrender_list[i][j])

        # Nested for loops that place the numbers when surrender is clicked
        # self.w.create_text outputs all the numbers in surrender_list one by one through count
        count: int = 0  # Used as an increment
        for x in range(50, 500, 100):
            for y in range(50, 500, 100):
                self.w.create_text(x, y, font="Calibri 24 bold",
                                   text=surrender_list1[count])
                count += 1
        self.counter +=1

    def next(self):
        # Reset the number choices and create the next puzzle
        count: int = 0
        self.counter += 1
        while count < 3:
            if self.counter < 3:
                self.lblPuz.set("Puzzle " + str(self.counter + 1))
                self.reset()
                self.create_widgets()
            else:
                messagebox.showinfo('KenKen', "You're out of puzzles!")
                self.counter == 0
                break
            count += 1

root = Tk()
root.title("KenKen")
root.geometry("600x660")
TheGUI(root)
root.mainloop()
