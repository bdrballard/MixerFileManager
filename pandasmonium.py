import pandas as pd
import csv
import globals
from filenaming import convertDay
from filenaming import convertMonth
from filenaming import findMonth
from filenaming import convertTime
from filenaming import convertYear
from filenaming import getFrameLabel


# This function perform analysis of the input file using pandas.
# It breaks the input file down into multiple input dataframes
# and saves each dataframe to a separate file destination.
# The user may need to specify these using a GUI.

# Parameters include  the input file name and path,
# output file name and path

def dataframeseparator(input_file):
    input_file = '/Users/danballard/Desktop/' + '2111190013.csv'
    print('Welcome to dataframeseparator')
    print("@input file name:%s" % input_file)
    # Step through the whole mixer file and determine the last line in the file
    csv_data = csv.reader(open(input_file))
    # The variable last_row is the index number for the last row in the file
    i = 0
    for row in csv_data:
        i = i + 1
        last_row = i

    last_row = last_row - 2  # adjust for extra header rows
    print("last row:%s" % last_row)
    # Now, using pandas, read the whole file and create one
    # or more dataframes for it.

    df = pd.read_csv(input_file)
    print(df)
    # determine how many dataframes are in the file
    n = 0
    frame_counter = 0  # first frame is missed in count
    for i in range(0, last_row - 1):
        n = n + 1
        item = df.iloc[i, 0]

        if item == 'Machine Sn':
            found_start_index = n
#           next_start_index = n
            found_first_header = df.iloc[n, 5]
            frame_counter = frame_counter + 1
            print("found_first_header_1:%s" % found_first_header)
    # now process the first frame
    n = 0
    for i in range(1, last_row - 1):
        n = n + 1
        item = df.iloc[n, 0]
        if item == 'Machine Sn':
            found_start_index = n
            next_start_index = n
            found_first_header = df.iloc[n, 5]
            print("found_first_header_2:%s" % found_first_header)
    next_frame: object = df.iloc[1:next_start_index, 0:6]

    print("print first frame:%s" % next_frame)

#    first_frame.to_csv(globals.NEW_FRAME_FILE_PATH + 'temp0.csv')
#    frame_label = getFrameLabel(globals.NEW_FRAME_FILE_PATH + 'temp0.csv')
#    output_file_name = globals.NEW_FRAME_FILE_PATH+frame_label + '-0.csv'
#    print("***output_file_name:%s" % output_file_name)
#    csv_data = first_frame.to_csv(output_file_name)

    # Now process any subsequent frames in the file
    found_end_index = 0
    for j in range(1, frame_counter):

        # iterate through this loop looking for the next 'Machine Sn'.  This
        # will be in the next data frame and can be used to mark the end
        # of the current frame
        for i in range(next_start_index, last_row - 1):
            item = df.iloc[next_start_index, 0]
            if item == 'Machine Sn':  # find the next 'Machine Sn' tag
                found_header = df.iloc[next_start_index, 5]
                found_end_index = next_start_index - 1
                next_start_index = next_start_index + 1
            else:
                next_start_index = next_start_index + 1
        found_end_index = next_start_index
        print("found_current_time:%s" % found_header)
        next_frame = df.iloc[found_start_index:found_end_index, 0:6]
        print("*************************************")
        print("next_start_index:%s" % next_start_index)
        print("found_start_index:%s" % found_start_index)
        print("found_end_index:%s" % found_end_index)
        print("*************************************")
    # create a temporary holding file for finding the new frame filename.
#       dfg_csv_data = new_frame.to_csv(globals.NEW_FRAME_FILE_PATH+'temp1.csv')

    frame_label = getFrameLabel(globals.NEW_FRAME_FILE_PATH)
    print("frame label 1:%s" % frame_label)

    # create a new output file name
    output_file_name = frame_label + '.csv'
    print("***----output_file_name:%s" % output_file_name)
            # print(EQUIPMENT_DESIGNATOR)
    # output_file_name = EQUIPMENT_DESIGNATOR + new_year + new_month + new_day + new_time
    print("************************%s" % output_file_name)
    #  The following operation occur in order to remove the header
    #  and create a new one.  The first row of the dataframe is
    #  assigned to the new_frame columns using the new_frame.iloc[0]
    #  statement.  Next the dataframe is sliced from the second row
    #  using its index 1 and assigned to the dataframe index.  This will
    #  remove the first row with index 0 from the dataframe.  Thus, the
    #  header of the dataframe is replaced with the first row of
    #  the dataframe

 #   new_frame.columns = new_frame.iloc[0]
 #   new_frame = new_frame[1:]
 #  new_frame.head()

    print ("frame_counter:%d" % frame_counter)
    print("printing new frame")
    print(next_frame)

# save the dataframe as a csv file
    bfg_csv_data = next_frame.to_csv(output_file_name)
    print("Ending j loop")
    return()
