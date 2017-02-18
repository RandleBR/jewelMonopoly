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
from pprint import pprint

def getPrizes():
    print("the cwd is " + os.getcwd())
    with open(os.getcwd() + "/prizes.json", 'r') as f:     
        prizes = json.load(f)
    return prizes

def getPrizeIndex(t, prizes):
    for idx, row in enumerate(prizes['prizes']): 
        #print(row['prize'])
        if row['prize'] == t:
            return idx
    return None

prizes = getPrizes()
pprint(prizes)

# get the current path?
filename = os.getcwd() + "\monopoly_tickets.txt"

target = open(filename, 'a')

ticket_in = input("Enter ticket number (2 left and 1 righmost characters): ")
ticket_prize = ticket_in[:2].lower()
prize_ticket_index = getPrizeIndex(ticket_prize, prizes)
if prize_ticket_index == None:
    print("Umm, I can't find a prize for " + ticket_prize)
    exit()
ticket_num = ticket_in[:-1].lower()
print("the tickets needed are:")
print(prizes['prizes'][prize_ticket_index]['tickets'])
print('And you win '+ prizes['prizes'][prize_ticket_index]['win'])


target.write("\n" + ticket_prize + ticket_in[:-1].lower())  # CHanged this to have the newline character before the ticket number


