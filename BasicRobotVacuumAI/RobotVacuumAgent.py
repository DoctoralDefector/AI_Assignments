#import random
import math
# name: Blake Gerold
# description: the agent works by finding the nearest dirty spot on the floor and cleaning it. It is rational because it takes
#              less actions to clean the floor than their is spots for both of the rooms. The only way for the robot to be more
#              rational is if it could plot the shortest path possible between all the dirty spots.
# proposed points: (10 out of 10)
#                 5 points: It peforms way better than the wandering bot
#                 3 points: My robot uses few moves than the total number of space: (17 vs 25 spots) for room and (14 vs 24) spots for room2
#                 2 points: Answered this question correctly in the description above

class RobotVacuumAgent:

    def __init__(self,filename):
        """
        init function establishes board, robotRow, robotCol
        :param filename: establishes board
        """
        with open(filename, "r") as file:
            self.board = [[x for x in line.split()] for line in file]

        self.num_spaces = 0 # number of potential clean/dirty spaces in board

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                self.num_spaces += 1
                if self.board[r][c] == '@' or self.board[r][c] == '!': # find the location of the robot
                    self.robotRow = r;
                    self.robotCol = c;


    def print(self):
        """
        displays board to console
        """
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                print(self.board[r][c], end = ' ')
            print()


    def do_something(self): #change this here
        """
        TODO: Implement this funtion with more intelligence
        Loops are not allowed (in this function
        can suck up dirt or move robot
        """
        if self.board[self.robotRow][self.robotCol] == '!':
            self.board[self.robotRow][self.robotCol] = '@'; #just sucked up the dirt

        else:#if the current location of the spot isn't dirty
            closesDirty = self.closesDirty() #sets a variable to be a array of the closesDirty function
            
            r = closesDirty[0] #row coordinates are the first spot in the array
            c = closesDirty[1] #column coordinates are the first spot in the array
            if r < self.robotRow: #triggers if the row coordinates for the nearest dirty number is less than the robot row coordinates
                self.move_up() #moves the bot up
            if r > self.robotRow: #triggers if the row coordinates for the nearest dirty spot is greater than the robot row coordinates
                self.move_down() #moves the bot down
            if c < self.robotCol: #triggers if the col coordinates for the nearest dirty number is less than the robot row coordinates
                self.move_left() #moves the bot left
            if c > self.robotCol: #triggers if the col coordinates for the nearest dirty spot is greater than the robot row coordinates
                self.move_right() #moves the bot right
            
            
    def out_of_bounds(self, row, col):
        """
        :param row:
        :param col:
        :return: True if (row,col) will be out of bounds of self.board
                otherwise, returns False
        """
        try:
            if row < 0 or row >= len(self.board) or col < 0 or col >= len(self.board[row]):
                return True
            else:
                return False
        except:
            print('exception occurred -- out of bounds')
            return True


    def move_up(self):
        """
        moves robot 1 space up (north)
        :return:
        """
        if not self.out_of_bounds(self.robotRow -1, self.robotCol):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotRow -= 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'

    def move_down(self):
        """
        moves robot 1 space down (south)
        :return:
        """
        if not self.out_of_bounds(self.robotRow+1, self.robotCol):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotRow += 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'


    def move_left(self):
        """
        moves robot 1 space left (west)
        :return:
        """
        if not self.out_of_bounds(self.robotRow, self.robotCol-1):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotCol -= 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'


    def move_right(self):
        """
         moves robot 1 space right (east)
         :return:
         """
        if not self.out_of_bounds(self.robotRow, self.robotCol+1):
            if self.board[self.robotRow][self.robotCol] == '@':
                self.board[self.robotRow][self.robotCol] = '.'
            elif self.board[self.robotRow][self.robotCol] == '!':
                self.board[self.robotRow][self.robotCol] = '*'
            self.robotCol += 1
            if self.board[self.robotRow][self.robotCol] == '*':
                self.board[self.robotRow][self.robotCol] = '!'
            elif self.board[self.robotRow][self.robotCol] == '.':
                self.board[self.robotRow][self.robotCol] = '@'


    def utility(self):
        """
        :return: the number of clean spots in the room
        """
        result = 0
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == '.' or self.board[r][c] == '@':
                    result += 1
        return result

    def is_goal(self):
        """
        :return: True if all of the spaces are clean; otherwise, False
        """
        if self.utility() == self.num_spaces:
            return True
        else:
            return False
    
    
    def closesDirty(self):
        lowest_d = float('inf') #sets lowest distance between bot and dirty spot to infinity
        rLoc = 0 #declares a integer to track the row location of the dirt
        cLoc = 0 #declares a integer to track the column location of the dirt

        for r in range(len(self.board)): #traverses the rows on the board
            for c in range(len(self.board[r])): #traverses the columns on the board
                if self.board[r][c] == '*': #triggers if the traversals land on dirt
                    d = math.sqrt(float((r-self.robotRow)**2) + float((c-self.robotCol)**2)) #calculates the distance between the bot and the dirt
                    if d < lowest_d: #triggers if a new lower distance is found
                        lowest_d = d #tracks the new lowest d
                        rLoc = r #row locations of the lowest d
                        cLoc = c #column locations of the lowest d
        return [rLoc, cLoc] #returns the location of the closest dirty spot as an array

if __name__ == '__main__': #DO NOT TOUCH!!!
    # create agent
    agent = RobotVacuumAgent("room2.txt")

    count = 0; # number of time steps

    # run the vacuum until room is clean
    while not agent.is_goal():
        print(count)
        agent.print()

        count += 1
        agent.do_something()

    # final state
    print(count)
    agent.print()
    
#Explain how your robot is more rational