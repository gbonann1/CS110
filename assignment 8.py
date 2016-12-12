"""
Gianluca Bonanno  
Assignment 8

Analysis
Write a program that converts entire files of unsigned decimal integers
  (base 10) to the base requested (between 2 and 16) OR unsigned integer
  values in some other base (between 2 and 16) to decimal (base 10),
  - given the file name, operation (to decimal or to base), and base  
  - as long as the user chooses to continue
  - for any valid integer in the given base
  - Note:  valid decimal integers may contain only the digits 0-9.
    Valid representations of values in other bases contain only the 
    string representation of digits that exist in that base.
    Invalid  file data should be converted to the string "BAD CODE".
  - Each line in the input files may contain multiple values
 
Output TO file:
- INVALID - data item to be written to file in place of invalid
            input file data item (str)
- newFile - contains converted values from input file
            (_io.TextIOWrapper, i.e., a text file)

Constants Given:  
- Note:  some of the following data structures map decimal to hex
  representations and vice versa since 16 is largest base that 
  this program must handle
- BASE_PROMPT - Prompt associated with operation (dict)
- MIN_BASE - lowest base that program handles, i.e., binary (int)
- MAX_BASE - highest base that program handles, i.e., hex (int)
- BASE_10 - integer base for decimal numbers
- ALL_BASE_CHARS - ordered set of all valid base digits (list)      
- DECIMAL_TO_BASE - maps decimal vals to hex representation (dict)
- BASE_TO_DECIMAL - maps hex representation to decimal vals (dict)
- INVALID - String used for output when input invalid
- OPERATIONS - Associates given operation with output file label
- FILE_EXT - Identifies .txt extension
- READ_MODE - file read operation
- WRITE_MODE - file write operation

Input FROM keyboard
- fileName (str)
- baseStr(str)
- operationStr - 'd' to decimal or 'b' to base (str)

Input FROM file
- newFile - contains data to be converted (_io.TextIOWrapper, i.e., text file)

Tasks (allocated to functions where noted)
- Validate inputs:
- - fileNameValidated() - function to validate input file name
- - operationIsValid - function to validate operation requested
- - baseIsValid - function to validate base requested
- - numberIsValid - function to validate data item in input file (Is it possible
      for this number to exist in the base the file claims to be in?)

- Prepare arguments:
- - convert base to int
- - convert decimal input items to int
- - makeName() - generate output file name given old file name, base 
    and operation requested

- Process Lines:
- - processList() - Same idea as in your last assignment
- - processLine() - Same idea as in your last assignment

- Process Data:
- - toBase() - convert a single decimal number (int) to its representation
      in the requested base (str)
- - toDecimal() - convert a single string representing a number in a given
      base (str) to its decimal representation (int)

- Process files:
- - open and close input and output files
- - read input file into list of strings
- - write each line of output to file
"""

# Incorporate OS path module
import os.path

# Initialize constants ------------------------------------------------

# Prompts
BASE_PROMPT = { 'd' : "Enter the base whose values are to be converted:  ", 
    'b': "Enter the base to which the values are being converted:  "}

# Range of bases that this program handles
MIN_BASE = 2
MAX_BASE = 16
BASE_10 = 10

# Allowable values
ALL_BASE_CHARS = '0123456789ABCDEF'

# decimal values mapped to bases 2-16 representations
DECIMAL_TO_BASE = {0 : '0',  1 : '1',  2 : '2',  3 : '3', 4 : '4',
                   5 : '5',  6 : '6',  7 : '7',  8 : '8', 9 : '9',
                  10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D',
                  14 : 'E', 15 : 'F'}

# base 2-16 representations mapped to decimal values
BASE_TO_DECIMAL = {'0' :  0, '1' :  1, '2' :  2, '3' : 3,  '4' : 4,
                   '5' :  5, '6' :  6, '7' :  7, '8' : 8,  '9' : 9,
                   'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13,
                   'E' : 14, 'F' : 15}

# Invalid data item
INVALID = "BAD_CODE "

# Mapping of valid operations to str descriptions
OPERATIONS = {'d':"ToDecimalFromBase", 'b': "FromDecimalToBase"}

# Required file extension
FILE_EXT = ".txt"

# File processing modes
READ_MODE = 'r'
WRITE_MODE = 'w'

# Function definitions ------------------------------------------------

# Checks that file exists and that extension is .txt
# param fileName (str)
# invokes isFile()from module os.path, endswith()
# return True when valid, False otherwise (bool)
def fileNameValidated(fileName):
    return os.path.isfile(fileName) and fileName.endswith(FILE_EXT)

#Returns true if the operation is d or b
#Else returns false
def operationIsValid(operationStr):
    return operationStr in OPERATIONS

#Returns true if the base is between 2 and 16 inclusive
#Else returns false
def baseIsValid(baseStr):
    return baseStr.isdigit() and int(baseStr) >= MIN_BASE and int(baseStr) <= MAX_BASE

#Returns true if the number is a possible value for the given base
#Else returns false
def numberIsValid(numberStr, base):
    return numberStr in ALL_BASE_CHARS[0:base]



# Generates output fileName from input fileName, base and operation
# param fileName (str)
#       opStr - requested operation (str)
#       base (int)
# invokes str.split(), str.replace(), str.join()
# return output fileName (str)
def makeName(fileName, opStr, base):
    nameList = fileName.split(".")
    nameList[0] += OPERATIONS[opStr] + str(base)
    return ".".join(nameList)


# convert a single decimal number (int) to its representation
# in the requested base (str)
# calculates the number of digits (maxIndex)
# uses modulus division to create the number in reversed order
# sets newNumber equal to the reversedNumber reversed
# Returns newNumber a string with the number followed by a space
def toBase(oldNumberStr, base):
    for i in range(len(oldNumberStr)):
        if not numberIsValid(oldNumberStr[i], BASE_10):
            return INVALID
    number = int(oldNumberStr)
    reversedNumber = ""
    maxIndex = 0
    slotValue = base**maxIndex
    while number > base**maxIndex:
        maxIndex += 1
    for i in range(maxIndex):
        newDigit = number % base
        number = number // base
        reversedNumber = reversedNumber + DECIMAL_TO_BASE[newDigit]
    newNumber = reversedNumber[::-1] + " "
    return newNumber  
    

# convert a single string representing a number in a given
# base (str) to its decimal representation (int)
# Returns newNumber, a string with the number followed by a space
def toDecimal(oldNumberStr, base):
    newInt = 0
    for i in range(len(oldNumberStr)):
        if not numberIsValid(oldNumberStr[i], int(base)):
            return INVALID
        else:
            indexValue = BASE_TO_DECIMAL.get(oldNumberStr[i])
            slotValue = base**(len(oldNumberStr)-1-i)
            newInt = newInt + (indexValue * slotValue)
            newNumber = str(newInt) + " "
    return newNumber

#Creates an empty string.
#Loops through the list of lines in the old file
#For each line in the oldFileList, it invokes and adds the result of processLine
#with the line as an argument to the empty string
#invokes processLine()
#Returns a string with all converted numbers from the file
def processList(oldFileList, operation, base):
    convertedNumbers = ""
    for i in range(len(oldFileList)):
        convertedNumbers = convertedNumbers + processLine(oldFileList[i], operation, base)
    return convertedNumbers   

#Creates an empty string
#Splits the line by each space and removes line break characters
#Loops through each number in the line and invokes toBase or toDecimal
#depending on the type of conversion requested
#returns the converted line
def processLine(oldLine, operation, base):
    newLine = "" 
    lineList = oldLine.split()
    while "\n" in lineList:
        lineList.remove("\n")
    if operation == 'b':
        for i in range(len(lineList)):
            newLine = newLine + toBase(lineList[i], base)
    else:
        for i in range(len(lineList)):
            newLine = newLine + toDecimal(lineList[i], base)
    return newLine
    
    
            
# Main function -----------------------------------------------------

# Converts contents of file, given file name, base, and desired 
# operation, and outputs converted contents to new file.
# When decimal values, converted to the representation of these values
# in given base.
# Otherwise, contents are representations of values in base given,
# and are converted to decimal
# invokes processList(), baseIsValid(), operationIsValid(), and fileNameValidated()
def main():
  
  # Describe program
  print("This program converts decimal values to a different base " + \
        "\nand representations of values in other bases to decimal" + \
        "\nBases must be within the ranges of 2 through 16, and "   + \
        "\nall values are input from file and output to file")

  # Read in file name
  fileName = input("Please enter a file name :")
  
  # As long as user provides file name
  while fileName:
    # validate file name
    #while not fileNameValidated(fileName):
        #print("Error, file not valid")
        #fileName = input("Please enter a file name :")
    
      
    # Get remaining inputs, validate and convert as necessary  
    print("Would you like to convert contents of file to decimal OR")
    print("would you like to convert contents of file to some other base?")
    operationStr = input("Press d for 'to decimal' or b for 'to other base :")
    while not operationIsValid(operationStr):
        print("Error, operation not valid")
        operationStr = input("Press d for 'to decimal' or b for 'to other base :")
    baseStr = input(BASE_PROMPT[operationStr])
    while not baseIsValid(baseStr):
        print("Error, base not in range")
        baseStr = input(BASE_PROMPT[operationStr])
            
    # Open input file, read contents into list and close file
    try:
        oldFile = open(fileName, READ_MODE)
        try:
            oldFileList = oldFile.readlines()
    

    # Process list
            output = processList(oldFileList, operationStr, int(baseStr))
    

    # Generate output file name
            newFileName = makeName(fileName, operationStr, baseStr)

    # Open output file, write each list item to file and close the file
            try:
                newFile = open(newFileName, WRITE_MODE)
                try:
                    newFile.write(output)
                    
                except IOError as err: # inner exception handler for outfile processing
                    print("\nProblem writing data: \n" + str(err))
                except ValueError as err:  # inner exception handler for outfile processing
                    print("\nProblem writing data, wrong format or corrupted?  \n" + str(err) + '\n')
                except Exception as err: # inner exception handler for outfile processing
                    print("\nData cannot be written to file: \n" + str(err) + '\n')
                finally:# will close file whether or not exception has been raised
                    newFile.close()

            except IOError as err: # "outer" exception handler for outfile open
                print("\nExecption raised during open of output file, no write performed: \n" + str(err) + '\n')

        except IOError as err: # inner exception handler for infile processing
            print("\nProblem reading data: \n" + str(err))
        except ValueError as err: # inner exception handler for infile processing
            print("\nProblem processing data, wrong format or corrupted? \n" + str(err) + '\n')
        except Exception as err: # inner exception handler for infile processing
            print("\nData cannot be read:  \n" + str(err) + '\n')        
        finally:# will close file whether or not exception has been raised
            oldFile.close()
    except FileNotFoundError as err:  # outer exception handler for infile open
      print("\nFile not found:  deleted or in wrong folder?  \n" + str(err) + '\n')
    except IOError as err: # outer exception handler for infile open
      print("\nException raised during open of input file, try a different file: \n" + str(err) + '\n')
    
 

    # Prompt user for another file name
    fileName = input("Please enter another file name or <enter> to quit: ")

main()
