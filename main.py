from urllib.request import urlretrieve
import re
import operator
from os import path

clean = []
ct_filenames = {}#dictionary of filenames
permonth = {}# dictionary of entries per month
perday = {}# dictionary of days and amount of transactions per day
list_dates = []#list of dates 12/Oct/1994
codes = []#list of status codes
redirects = 0 #counts the times 3xx code appears
notsuccess = 0 #counts the times 4xx comes up

#Puts various log entry pieces into a dictionary
class Totals:
    def __init__(self, x, list):
      self.x = x
      self.list = list
      if x in list:
        list[x] += 1
      else:
        list[x] = 1

#splits each line in log file to be put into dictionary 
for line in open('clean_log.txt'):
  
  pieces = re.split(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*", line)
  codes.append(pieces[6])
  list_dates.append(pieces[1])
  date = pieces[1]# list of 12/Oct/1994
  month = date[3:12] # list of Oct/1994

  filename = pieces[4]# list of requested files

  months = Totals(month, permonth)
  files = Totals(filename, ct_filenames)
  days = Totals(date, perday)

#prints the total transactions per month
for key in months.list:
  print ("In " + key + " there was " + str(months.list[key]) + " transactions")

print("\nThis log includes log entries from " + list_dates[0] + " to " + list_dates[len(list_dates)-1])#gives the user fill range of adtes the log file covers

#asks user if they would like to get total transaction on a certain day
while True:    
    n = input("\nWould you like to find the number of transaction on a certain day(Y or N): ")
    if n == "N":
        break  # stops the loop
    elif n == "Y":
        d = str(input("\nWhat day would you like to see the total transactions for(ex. 12/Oct/1995): "))
        if d in days.list:
          print ("\nOn " + d + " there was " + str(days.list[d]) + " total transactions ")
        else:
          print("\nNo, key: " + d + " does not exists in dictionary. Please try again.")

#tallys up the number of redirects and not successful transactions
for numbers in codes:
	if(numbers[0] == '3'):
		redirects = redirects + 1
	if(numbers[0] == '4'):
		notsuccess = notsuccess + 1
		
	
#print percent of redirects and not success transactions
print("\nThe percent of not successful requests is " + str((notsuccess/len(codes))*100) + "%")
print("\nThe percent of redirected requests is "+ str((redirects/len(codes))*100)+ "%")

print('\nTotal logs in the file: ' + str(sum(days.list.values())))
print('\nMost requested file: ' + max(files.list.items(), key=operator.itemgetter(1))[0])
print('\nLeast requested file: ' + min(files.list.items(), key=operator.itemgetter(1))[0] + "\n")

while True:    
    n = input("\nWould you like to find the number of transaction within a certain time frame(Y or N): ")
    if n == "N" :
        break  
    elif n == "Y":
        while True:
            start = str(input("\nEnter your start date(ex. 12/Oct/1994)(to exit enter X): "))
            if start == "X":
                break
            end = str(input("\nEnter your end date, this date will not be included(ex. 12/Oct/1995): "))
            if ((start in list_dates) and (end in list_dates)):
                start_days_ct = list_dates.index(start)
                end_days_ct = list_dates.index(end)
                requests = end_days_ct - start_days_ct
                print('Between ' + start + ' and ' + end + ' there were ' + str(requests) + ' requests.')   
                break
            else:
                print("\nThis time frame does not exists in file. Please try again.")



FILE_NAME = 'clean_log.txt'

#checks if user would like to create a txt file for each month
while True:    
    n = input("\nWould you like to split the log file up by month(Y or N)?(WARNING: this may take a while): ")
    if n == "N":
        break  # stops the loop
    elif n == "Y":
                # open file in append mode
        Oct94 = open("Oct94.txt", 'a+')
        Nov94 = open("Nov94.txt", 'a+')
        Dec94 = open("Dec94.txt", 'a+')
        Jan95 = open("Jan95.txt", 'a+')
        Feb95 = open("Feb95.txt", 'a+')
        Mar95 = open("Mar95.txt", 'a+')
        Apr95 = open("Apr95.txt", 'a+')
        May95 = open("May95.txt", 'a+')
        Jun95 = open("Jun95.txt", 'a+')
        Jul95 = open("Jul95.txt", 'a+')
        Aug95 = open("Aug95.txt", 'a+')
        Sep95 = open("Sep95.txt", 'a+')
        Oct95 = open("Oct95.txt", 'a+')
	
    	for line in open(FILE_NAME):

        	regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

        	# Call the split() method to get all the capture groups put in a list
        	parts = regex.split(line)
    
        	date = parts[1]
        	clean = date[3:12]#clean up date
          
            
        	if clean == 'Oct/1994':
                	Oct94.write(line)
        	elif clean == 'Nov/1994':
                	Nov94.write(line)
        	elif clean == 'Dec/1994':
                	Dec94.write(line)
        	elif clean == 'Jan/1995':
                	Jan95.write(line)
        	elif clean == 'Feb/1995':
                	Feb95.write(line)
        	elif clean == 'Mar/1995':
                	Mar95.write(line)
        	elif clean == 'Apr/1995':
                	Apr95.write(line)
        	elif clean == 'May/1995':
                	May95.write(line)
        	elif clean == 'Jun/1995':
                	Jun95.write(line)
        	elif clean == 'Jul/1995':
                	Jul95.write(line)
        	elif clean == 'Aug/1995':
                	Aug95.write(line)
        	elif clean == 'Sep/1995':
                	Sep95.write(line)
        	elif clean == 'Oct/1995':
                	Oct95.write(line)

	Oct94.close()
	Nov94.close()
	Dec94.close() 
	Jan95.close()
	Feb95.close()
	Mar95.close()
	Apr95.close()
	May95.close()
	Jun95.close()
	Jul95.close()
	Aug95.close()
	Sep95.close()
	Oct95.close()
	print('All files have been created')
