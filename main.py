# main for processing Flacktek Mixer data files

# These may become GUI input elements
# from csvreader import getcsvHeader
import csv
import tkinter
import os
import globals

from filenaming import convertDay
from filenaming import convertMonth
from filenaming import findMonth
from filenaming import convertTime
from filenaming import convertYear
from pandasmonium import dataframeseparator
from filenaming import getFrameLabel

# This program reads files created by the Flacktek during the mixing process.
# Each file contains data for one or more mixer operations.  Each of these
# data runs is referred to as a "data frame."  Each Flacktek file is a .csv file
# titled with the serial number of the mixer  - e.g. 211190013.csv.

# We define the location of the Flacktek data file as a path called raw_file_path.
# This will need to be changed on an operational system.
def getRawFileLocation():
    raw_file_path = globals.RAW_FILE_PATH
    raw_file_name = globals.RAW_FILE_NAME
    raw_file_location = raw_file_path + raw_file_name
    return raw_file_location


def getNewFrameLocation(frame_filename):
    new_frame_file_path: str = globals.NEW_FRAME_FILE_PATH
 #   new_frame_file_name = frame_filename
    new_frame_file_location = new_frame_file_path + frame_filename
    return new_frame_file_location

if __name__ == '__main__':
    globals.initialize()

# Read the raw mixer file and get the header information for creating the output

#tkinter._test()
#  The method 'getFrameLabel' reads the specified csv file
#  and creates a filename for subsequently storing that file.
#  The filename is returned.

input_file_name = globals.RAW_FILE_PATH + globals.RAW_FILE_NAME
print ("input file name enter:%s" % input_file_name)
# the 'dataframeseparator' generates any new dataframe files
# from the old raw file.
dataframeseparator(input_file_name)

print("completed dataframeseparator")
# os.remove(globals.NEW_FRAME_FILE_PATH+'temp.csv')