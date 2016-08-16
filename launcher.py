import subprocess
import logging

# Main program
logging.basicConfig()
process = subprocess.Popen(["python", "filter.py"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = process.communicate("Processing ...")
print ('########## Standard output : ')
print out
#print ('########## Standard error : ')
#print err





