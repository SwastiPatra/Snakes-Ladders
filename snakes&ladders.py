# Importing Libraries
import random


# Snake Class
class Snake:
    """
    Class to Implement Snakes and Ladders Game.
    """

    # Default Constructor
    def __init__(self):

        print("###### Welcome to Snakes & Ladders Game ######")
        self.name1 = input("Enter the Name of Player 1 : ")                #To input name of Player 1
        self.name2 = input("Enter the Name of Player 2 : ")                #To input name of Player 2
        print("###### Let us Start ######")
        self._game = [0, 0]                                                # Steps of the Players in the beginning

        self.__snakes = {17: 7, 54: 34, 62: 19, 98: 79}
        self.__ladders = {3: 38, 24: 33, 42: 93, 72: 84}

    # Display Players' Name
    def displayName(self):

        print(f"Player 1's Name : {self.name1}, Player 2's Name : {self.name2}")

    # Display Winner's Name
    def __displayWinner(self, number):

        if number == "1":
            winner = self.name1
        else:
            winner = self.name2
        print(f"Player {number} won the Game!!!")
        print(f"Congratulations {winner} !!")
        print("###### Game Successfully Finished ######")
        exit(0)

    # Check for Any Snakes or Ladders in the current position
    def __checkSnakeLadder(self, position):

        if position in self.__snakes.keys():
            position = self.__snakes.get(position)
        elif position in self.__ladders.keys():
            position = self.__ladders.get(position)

        return position

    # Checking for "quit" condition
    def __quit(self, number):

        if number == "1":
            self.__displayWinner("2")
        else:
            self.__displayWinner("1")
        exit(0)

    # Check for Overflow Position
    def __Hundred(self, position, j):

        if (position + j) > 100:
            pass
        else:
            position += j

        return position

    # Check for the Range of Input in Manual Mode
    def __checkManualMode(self, inp):

        j = int(inp)
        if j not in range(2, 20):
            print("Invalid Input! The Number you Entered isn't within the range of between 1 and 20")
            try:
                j = int(input("Please Enter a Number within the given Range : "))
                self.__checkManualMode(j)
            except:
                j = int(input("Please Enter a Valid Number within the given Range : "))
                self.__checkManualMode(j)

        return j

    def __checkInput(self, number):

        global j
        inp = input(f"Player {number} : ")
        self.__checkManualMode(j)
        if inp == "roll":
            j = random.randint(1, 6)
        elif inp == "quit":
            self.__quit(number)
        elif inp.isnumeric():
            j = self.__checkManualMode(inp)
        else:
            print("Illegal Input, Please Input a Valid Input !")
            j = self.__checkInput(number)
        print("You got a ", j)

        return j

    # Player Position Function
    def __playerPosition(self, number):

        pos = 0
        pos = self._game[int(number) - 1]
        j = self.__checkInput(number)                 # Check for Valid Input
        pos = self.__Hundred(pos, j)                  # Check for the Validity of the Position
        pos = self.__checkSnakeLadder(pos)            # Check for Snakes and Ladder
        print(" Your Final Position is ", pos)
        if pos == 100:                                # Check for Winner
            self.__displayWinner(number)
        self._game[int(number) - 1] = pos

    # Snake Game Function
    def snakeGame(self):

        while True:
            self.__playerPosition('1')
            self.__playerPosition('2')


# Main Method
if __name__ == "__main__":
    # Using Exception Handling Techniques to Handle any unfavourable outcomes
    snake = Snake()
    snake.displayName()
    snake.snakeGame()             # Game Method
    del snake                     # Delete the Object


