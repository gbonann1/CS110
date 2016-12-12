#Gianluca Bonanno, Assignment 5, Excercise 1

import random
import turtle
import math

NUM_VALUES = 14
MAX_VALUE = 10

#Reads in a list, adds each number in the list and divides it by the number
#of total items in the list. Returns the resulting mean.
def mean(alist):
    mean = sum(alist)/len(alist)
    return mean

#Invokes the mean function
#Calculates and returns the standard deviation of a list
def stanDev(alist):
    theMean = mean(alist)

    total = 0
    for item in alist:
        difference = item - theMean
        diffsq = difference ** 2
        total = total + diffsq

    sdev = math.sqrt(total/(len(alist)-1))
    return sdev

#Invokes the stanDev function and the mean function.
#Takes in a list and creates a dictionary from the items in the list.
#Then creates a frequency chart that displays the number of occurences
#of each value.
#Displays the mean of the values with a red line.
#Displays one standard deviation above and below the mean with blue lines.

def frequencyChart(alist):

    #Creates a dictionary from the numbers in the list and their occurences
    #Starts by setting the occurences of all integers from 0 to MAX_VALUE to 0
    countdict = {}

    for i in range(MAX_VALUE):
        countdict[i] = 0
        
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1

    itemlist = list(countdict.keys())
    minitem = 0
    maxitem = len(itemlist)-1

    countlist = countdict.values()
    maxcount = max(countlist)

    #Creates the graph and draws the x axis
    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1,-1,maxitem+1,maxcount+1)
    chartT.hideturtle()
    chartT.up()
    chartT.goto(0,0)
    chartT.down()
    chartT.goto(maxitem,0)
    chartT.up()

    #Writes the maximum y value along the y axis
    chartT.goto(-1,0)
    chartT.write("0", font=("Helvetica",16,"bold"))
    chartT.goto(-1,maxcount)
    chartT.write(str(maxcount),font=("Helvetica",16,"bold"))

    #Writes the values on the x axis of the graph by looping through
    #each item in the list.
    for index in range(len(itemlist)):
        chartT.goto(index,-1)
        chartT.write(str(itemlist[index]),font=("Helvetica",16,"bold"))

        chartT.goto(index,0)
        chartT.down()
        chartT.goto(index,countdict[itemlist[index]])
        chartT.up()

    #Draws a red line to represent the mean and displays the mean
    chartT.color("red")
    chartT.goto(mean(alist),0)
    chartT.down()
    chartT.goto(mean(alist),maxcount)
    chartT.write(str(mean(alist)),font=("Helvetica",16,"bold"))
    chartT.up()
    #Draws blue lines to represent 1 standard deviation above and below the mean
    chartT.color("blue")
    chartT.goto(mean(alist)+stanDev(alist),0)
    chartT.down()
    chartT.goto(mean(alist)+stanDev(alist),maxcount)
    chartT.write(str(mean(alist)+stanDev(alist)),font=("Helvetica",16,"bold"))
    chartT.up()
    chartT.goto(mean(alist)-stanDev(alist),0)
    chartT.down()
    chartT.goto(mean(alist)-stanDev(alist),maxcount)
    chartT.write(str(mean(alist)-stanDev(alist)),font=("Helvetica",16,"bold"))
    
    wn.exitonclick()

#Creates a randomly generated list and tests the program with that list.
def main():
    #testList = []
    #for i in range(NUM_VALUES)
        #testList.append(random.randint(1, MAX_VALUE))
    #print(testList)    #Debug     
    testList = [0,1,1,2,2,3,5,5,5,6,7,9,9,10]
    frequencyChart(testList)
    
main()
