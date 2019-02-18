#-------------------------------------------------------------------------------
# Ken_Lee_Project_CLASS.py
# Name: Ken Lee
# Python Version: 3.6.4
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References:
#-------------------------------------------------------------------------------
# Comments to grader:
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------


class KenKen:
    def __init__(self):
        # A big list that holds 3 puzzles
        self.puzzlelist = [['11+', '', '', '', '', '2/', '', '5', '11+', '', '5', '16x', '',
                            '20x', '', '4+', '', '', '', '', '2/', '', '1-', '', '5'],
                           ['45x', '', '', '7+', '',
                            '1-', '', '5', '', '3+', '', '9+', '', '9+', '', '2/', '', '', '', '', '', '16x', '',
                            '11+', ''],
                           ['11+', '', '', '', '9+', '15x', '', '', '9+', '', '', '8+', '', '', '', '5+',
                            '8+', '225x', '', '', '', '', '', '', '']]

        # Lines of the puzzle
        self.lines1 = [[100, 0, 100, 400], [200, 0, 200, 400], [300, 0, 300, 200],
                       [300, 400, 300, 500], [400, 0, 400, 400], [200, 100, 300, 100], [100, 200, 200, 200],
                       [300, 200, 500, 200], [100, 300, 400, 300], [0, 400, 100, 400], [200, 400, 300, 400],
                       [400, 400, 500, 400], [400, 400, 400, 500]]

        self.lines2 = [[100, 0, 100, 100], [100, 200, 100, 300], [100, 400, 100, 500],
                       [200, 100, 200, 400], [300, 0, 300, 100], [300, 200, 300, 300],
                       [300, 400, 300, 500], [400, 100, 400, 200], [400, 300, 400, 400], [100, 100, 500, 100],
                       [100, 200, 200, 200], [300, 200, 400, 200], [0, 300, 500, 300], [100, 400, 400, 400]]

        self.lines3 = [[100, 0, 100, 400], [200, 100, 200, 200], [200, 400, 200, 500],
                       [300, 0, 300, 400], [400, 200, 400, 300], [400, 400, 400, 500],
                       [100, 200, 200, 200], [200, 100, 500, 100], [300, 200, 400, 200],
                       [100, 300, 300, 300], [400, 300, 500, 300], [0, 400, 200, 400], [300, 400, 400, 400]]

        # Holds all 3 solution lists
        self.solution = [[[3, 5, 2, 1, 4], [4, 2, 5, 3, 1], [5, 4, 1, 2, 3], [1, 3, 4, 5, 2],
                          [2, 1, 3, 4, 5]],
                         [[5, 1, 3, 2, 4], [4, 3, 5, 1, 2], [3, 5, 2, 4, 1], [1, 2, 4, 5, 3], [2, 4, 1, 3, 5]],
                         [[2, 5, 3, 1, 4], [3, 1, 4, 2, 5], [5, 3, 1, 4, 2], [4, 2, 5, 3, 1], [1, 4, 2, 5, 3]]]

    def getpuzzles(self):
        puzzles = [self.puzzlelist]
        return puzzles
        # Gives GUI the current puzzle

    def getlines(self):
        # Gives the GUI the layout of the puzzle
        lines = [self.lines1, self.lines2, self.lines3]
        return lines

    def changer(self, event):
        # Changes the current user selection to another value
        row = int(event.x / 100)
        column = int(event.y / 100)
        return row, column

    def checkit(self, numberlist, number):
        return self.solution[number]

    def surrender(self, number):
        # Reveals the answer if player gives up
        return self.solution[number]

    def resetnum(self, checklist):
        return [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]