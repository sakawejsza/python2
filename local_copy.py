from urllib.request import urlretrieve
import re
from os import path


if path.isfile('log.txt') == False:

    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'log.txt'

    #Use urlretrieve() to fetch a remote copy and save into the local file path
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)

    if path.isfile('clean_log.txt') == False:
        FILE_NAME = 'log.txt'
        for line in open(FILE_NAME):

            file_name = 'clean_log.txt'
            fh = open(file_name, 'a+')  # open file in append mode

            
            # Use open() to get a filehandle that can access the file

            regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")

            # Call the split() method to get all the capture groups put in a list
            parts = regex.split(line)
            #date = parts[1]
            #clean up date
            #clean = date[3:12]
            # Let's see what the regex grabbed...
            # print (parts)
            
            # Sanity check the line -- there should be 7 elements in the list (remember that index 0 has the whole string)
            if parts and len(parts) >= 7:
                fh.write(line)
              
    print("Log files have been created")
else:
	print('You already have the log files.')
