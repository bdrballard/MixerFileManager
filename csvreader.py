#  This program imports the csv file and reads the Master Header which
#  must be prepended to all data files.  Definitions of the columns are
#  provided here.

import csv
import pandas as pd
import filenaming
import globals

from filenaming import convertDay
from filenaming import convertMonth

#  This method reads the raw cvs file and determines the information
#  required for naming the processed files
#   getcsvHeader(file_path: object, file_name: object) -> object:
#   print("in getcvsHeader")

#    csv_data = csv.reader(open(file_path + file_name))
csv_data = csv.reader(open('/Users/danballard/Desktop/2111190013.csv'))
master_header = next(csv_data)

machine_sn = master_header[1]
day_of_week = master_header[2]
month_and_day = master_header[3]
year = master_header[4]
time = master_header[5]
print(machine_sn, day_of_week, month_and_day, year, time)

the_month = convertMonth(month_and_day)
the_day = convertDay(month_and_day)
print("the month is: %s" % the_month)
print ("the day is: %s" % the_day)
 #   return

# print("Importing the CSV File ")

# The variable last_row is the index number for the last value in the file
i = 0
for row in csv_data:
    i = i+1
    last_row = i

last_row = last_row - 2   #adjust for extra header row

print("last row is  = %d" % last_row)


# now find the header with the date and time information in it
df = pd.read_csv('/Users/danballard/Desktop/2111190013.csv', names=master_header)
nums = df.head(1)  #
print("header follows")
print(nums)
last_row_of_run = df.tail(1)  # find the last row of data in a file
print(last_row_of_run)
print(last_row)

