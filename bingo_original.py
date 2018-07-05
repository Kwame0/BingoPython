import random # Include random library
import math # Include math library
import time # Include time library
import sys # Include System library                                                                                                                 [3.63]
Grid = [3,4]; # 3 * 4 is default | Numbers Can't Be Equal e.g [77,77] | This bug can be fixed with more time
GridSum = Grid[0] * Grid[1]; # Get the total sum of the Grid
ChosenNumbers = []; # Array of numbers user will choose
NumbersUsed = []; # Array of Numbers that have been picked after board as been set
Win = False; # Win Bool
mode = "Manual"; # Choose Manual or Automatic roll

# Tiny Bug Fix
if Grid[0] > Grid[1]: # If the first value in Grid array is bigger than the second
    temp = Grid[1]; # Create a temporary variable to hold the second array
    Grid[1] = Grid[0]; # The second array will be the first array
    Grid[0] = temp # The First array will be set to the temporary variable

def ValidateNum(num): # Partially Works - num will be the number to verify
    for x in range(1, GridSum): # for x = 1; while x is smaller than GridSum; x++
        if [x,num] in ChosenNumbers: # if ChosenNumbers[x,num] in ChosenNumbers
            return False 
        elif num < 1 or num > GridSum: # If num is smaller than 1 or bigger than GridSum
            return False
        else:
            return True
        
# Print Board Function
def PrintBoard():
    print("\n");
    print("======YOUR======");
    print("======BOARD=====");
    print("================ \n");
    colOutput = []; # Array to hold all the numbers that have been inputed into the board
    for col in range(len(ChosenNumbers)): # for col = 0; while col is smaller than length of ChosenNumbers; col ++
        colOutput.append(ChosenNumbers[col][1]);  # Add ChosenNumbers 2nd array to colOutput
        if len(colOutput) == Grid[0]: # If the length of colOutput equal to the length the degsinated row 
            #print(colOutput); # <- was used for debugging purposes
            output = ""; # Create the output string
            for num in range(len(colOutput)): # For every number in colOutput
                if colOutput[num] in NumbersUsed: # if the number is in NumbersUsed (Number that have been rolled)
                    output += "  " + "X" + "   "; # Cross it out
                else:
                    output += "  " + str(colOutput[num]) + "   "; # Print it out
                #print(colOutput[num]); # <- was used for debugging purposes
            print(output + "\n");
            colOutput = [];   # Clear row  
    print("================");
    #print("\n");

# Check Corners to win
def CheckCornersWin():
    NumbersOutput = []; # Array to hold all the numbers that have been inputed into the board 
    for col in range(len(ChosenNumbers)): # for col = 0; while col is smaller than length of ChosenNumbers; col ++
        NumbersOutput.append(ChosenNumbers[col][1]); # Add ChosenNumbers 2nd array to NumbersOutput
    if NumbersOutput[0] in NumbersUsed and NumbersOutput[Grid[0]-1] in NumbersUsed and NumbersOutput[-1] in NumbersUsed and NumbersOutput[-Grid[0]] in NumbersUsed:
        # If first and and end of the first row is in NumbersUsed AND the first and end of the last row is in NumbersUsed array then they win
        Win = True
        print("\n \n All Corners have been cleared! \n \n");
        PrintBoard();
        WinGame();


# Check columns to win
def CheckColumnWin():
    ColNum = []; # Create array to hold the number of columns in this grid
    Cols = []; # Create an array the will be 2d and hold the columns of the grid
    temporaryArray = []; # Array to hold all the numbers that have been inputed into the board 
    for col in range(len(ChosenNumbers)): # for col = 0; while col is smaller than length of ChosenNumbers; col ++
        temporaryArray.append(ChosenNumbers[col][1]); # Add ChosenNumbers 2nd array to temporaryArray

    for number in range(0, Grid[0]): # for number = 0; while number < is smaller than degsinated row size
        ColNum.append(temporaryArray[number]); # add the column number to temporaryArray

    for number in range(len(ColNum)): # for numer = 0; while number < the amount of columns in the grid; number ++
        curNum = ColNum[number]; # current Number is column number
        ColsPre = []; # Create an empty array to append into Cols array later
        ColsPre.append(curNum); # Add the first number into ColsPre

        startNum = temporaryArray.index(ColNum[number]); # Store the position of the first number in the column
        x = 0; # temporary int x
        while x < Grid[0]: # while x is smaller than the degsinated row size 
            startNum += Grid[0]; # go to the next number in the column by adding the size of a row
            #print(startNum)
            #print(temporaryArray[startNum])
            ColsPre.append(temporaryArray[startNum]); # Add this number into ColsPre
            x += 1; # x ++
        Cols.append(ColsPre); # add the full column into the array Cols
    ## Check Cols For Win
        for col in Cols: # for every column in the grid
            colWinCount = 0; # int to check how many numbers in the column are crossed out
            for num in col: # for every number in the column
                if num in NumbersUsed: # check if the number is crossed out
                    colWinCount += 1; # If it is crossed out, count it as ticked
            if colWinCount == Grid[1]: # if all ticked numbers in the column == (degsinated column size)
                Win = True # Win the game
                print("\n You have cleared a column! \n");
                PrintBoard();
                WinGame(); 
# Check rows to win
def CheckRowWin():
    Rows = []; # Create a 2d array to store all the rows
    temporaryArray = []; # Array to hold all the numbers that have been inputed into the board 
    for col in range(len(ChosenNumbers)): # for col = 0; while col is smaller than length of ChosenNumbers; col ++
        temporaryArray.append(ChosenNumbers[col][1]); # Add ChosenNumbers 2nd array to temporaryArray 
        if len(temporaryArray) == Grid[0]: # if the number of rows is the same as the degsinated row
            Rows.append(temporaryArray); # Add the temporaryArray to thr Rows array
            temporaryArray = []; # Reset array
    for Row in Rows: # for every row in the grid
        rowWinCount = 0; # int to check how many numbers in the row are crossed out
        for Number in Row: # for every number in the row
            if Number in NumbersUsed: # if the number is crossed out
                rowWinCount += 1; # if it is crossed out, count it as ticked
        if rowWinCount == Grid[0]: # if all ticked numbers in the row == (degsinated row size)
            Win = True # Win the game
            print("\n You have cleared a row! \n");
            PrintBoard();
            WinGame(); 
            
# Check to see if the number rolled has been used
def NumberRolled(num): # num is the number to verify
    if num in NumbersUsed: # if number has been rolled
        return False
    elif num < 1 or num > GridSum:
        return False
    else:
        NumbersUsed.append(num); # add the number to the roll list
        return True

# Win game function
def WinGame():
    print("\n \n \n Thank you for playing Richard's bingo! You have won! \n \n \n");
    sys.exit() # exit script

## Start the game - ask for numbers

while(len(ChosenNumbers) < GridSum): # while the amount of chosen numbers is smaller than the amount of avaliable spaces in the grid
    number = int(input("Pick a number? (0 - " + str(GridSum) + ")")); # ask for a number
    validated = ValidateNum(number); # ask for the number to be validated with this function and return the result and store it as validated
    if validated == True: # if the number has not been used and has passed all validated checks
        row = 0; # Row count is zero
        for i in range(0, len(ChosenNumbers)): # for i = 0; i < qty of numbers chosen; i++
            if i % Grid[0] == 0: # if the number can be divisible by (degsinated row size)
                row += 1; # add one to row  count
        # the for loop above will check what row we are on and use this to form the grid
        if row == 0: # if the row is zero (first few numbers check also bug fixing)
            if [1,1] == [1,number]: # if its the absolute number (bug fix)
                ChosenNumbers.append([Grid[1],number]); # insert it into the last row (bug fix)
            else:
                ChosenNumbers.append([1,number]); # insert it into the first row
        else:
            ChosenNumbers.append([row,number]); #  insert the number and the row it is on
        #print(ChosenNumbers); # <-- was used for debugging purposes
        PrintBoard(); # print the board once the number has been inserted
    else:
        print("Choose again");

# Make the board
PrintBoard();
if mode == "Manual":
    print("MODE: Manual Dice \n \n");
else:
    print("MODE: Automatic Dice \n \n");
    
while Win == False: # Needs Tiny fixing... (fixed by killing script)
    if mode == "Manual": # if the mode is manual ask for the number to be inputed
        inputnum = int(input("Enter the number chosen")); # get the input number
        status = NumberRolled(inputnum); # check if the number has been rolled
        if status == True: # if it has not been rolled
            CheckCornersWin(); # Check if they have won by corners
            CheckColumnWin(); # Check if they have won by columns
            CheckRowWin(); # Check if they have won by row
            NumbersPicked = []; # create an empty array
            for col in range(len(ChosenNumbers)): # for col = 0; while col < length of numbers we have chosen; col ++
                NumbersPicked.append(ChosenNumbers[col][1]); # add the number in chosennumbers to numbers picked
            if inputnum in NumbersPicked: # if the number rolled is in numbers we have picked, inform the player
                PrintBoard();
                print("We have crossed out " + str(inputnum) + " for you");
        else:
            print("Number already entered (Or out of range)");
            PrintBoard();
            #CornersLeft();
            #RowsLeft();
            #ColumnsLeft();
    else: # if the mode is automatic we will randomly generate the numbers to be called out
        roll = input("Enter any key to roll dice"); # wait for player to roll the dice with any input
        inputnum = random.randint(1, GridSum); # get the input number
        status = NumberRolled(inputnum); # check if the number has been rolled
        print("The roll was " + str(inputnum) + "\n");
        if status == True: # if it has not been rolled
            CheckCornersWin(); # Check if they have won by corners
            CheckColumnWin(); # Check if they have won by columns
            CheckRowWin(); # Check if they have won by row
            NumbersPicked = []; # create an empty array
            for col in range(len(ChosenNumbers)): # for col = 0; while col < length of numbers we have chosen; col ++
                NumbersPicked.append(ChosenNumbers[col][1]); # add the number in chosennumbers to numbers picked
            if inputnum in NumbersPicked: # if the number rolled is in numbers we have picked, inform the player
                PrintBoard();
                print("We have crossed out " + str(inputnum) + " for you");
        else:
            print("Number already used, reloading... \n");
            time.sleep(1.5);
            PrintBoard();
            #CornersLeft();
            #RowsLeft();
            #ColumnsLeft();
            


        
