'''
monopoly

input value
read first 2 chars
check all values
	if no match, log
	if match
		check last value
			if match don't log
			if no match log
				if a+b+c+d then declare winner


'''
import os
import json
import time

def getGameBoard():
    with open(os.getcwd() + "\gameBoard.json", 'r') as f:     
        return json.load(f)

def saveGameBoard():
    with open(os.getcwd() + "\gameBoard.json", 'w') as output:
        json.dump(gameBoard, output)
    output.close()
        

def getPrize(t, gameBoard):
    for idx, row in enumerate(gameBoard['gameBoard']): 
        if row['prize'] == t:
            return row
    return None

def addTicket(prize, index):
    for idx, row in enumerate(gameBoard['gameBoard']): 
        if row['prize'] == prize:
            row['have'][index] += 1

            saveGameBoard()

            # is this the winning ticket? (all have are >0)
            return 0 not in row['have']
    return False
    
# The gamBoard is a list of the prizes and the tickets already have
gameBoard = getGameBoard()

ticket_in = input("Enter ticket number (2 left and 1 righmost characters): ")

ticket_prize = ticket_in[:2].lower()
prize = getPrize(ticket_prize, gameBoard)
if prize == None:
    print("Umm, I can't find a prize for " + ticket_prize)
    exit()
if len(ticket_in) < 2:
    print("Umm, that ticket number isn't long enough")
    exit()

# What is the index of the prize?
ticket_num = ticket_in[-1:].lower()
ticket_index = None
try:
    ticket_index = prize['tickets'].index(ticket_num)
except ValueError:
    print("Umm, that ticket number isn't in the game Board?")
    exit()

# Determine if we have a winner!
print("You would win "+ prize['win'])

# Do we need that ticket for the board?
ticket_count = prize['have'][ticket_index]
if  ticket_count > 0:
    print("Nice try, we already have that seen that ticket " + str(ticket_count) + " times.")
else:
    print("Oh, we need that one! ")
    
# Add ticket to the tickets we have 
if addTicket(prize['prize'],ticket_index):
    print("WINNER !!! WooHoo! We have all of the tickets for " + prize['prize'])
    print("We get a " + prize['win'])

# Write the ticket to a log of tickets
filename = os.getcwd() + "\monopoly_tickets.txt"
target = open(filename, 'a')
target.write("\n" + ticket_prize + ticket_num + ',' + str(time.time()))  # CHanged this to have the newline character before the ticket number


