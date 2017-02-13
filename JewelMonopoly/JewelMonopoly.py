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

# get the current path?
filename = "C:\python\Monopoly\monopoly_tickets.txt"

print ("We're going to use %s" % filename)


target = open(filename, 'a')

ticket_num = input("Enter ticket number (2 left and 1 righmost characters): ")

target.write("\n" + ticket_num)  # CHanged this to have the newline character before the ticket number

