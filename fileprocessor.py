import csv
import pandas as pd




def foundheader(input_file, record_number):
    # This method returns true if the record_number
    # is a header, otherwise it returns false
    fields = []
    rows = []
    with open(input_file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        print (csvreader)
        fields = next(csvreader)
        record_number = record_number +1
        real_date =fields[5]
        real_year =fields[4]
        real_month_day = fields[3]
        recordf =fields[0]
        print("recordf:%s" % recordf)
        print("record number:%s" % record_number)
        if (recordf == 'Machine Sn'):
            return True
        else:
            return False

def copyrecord(input_file, output_file):
    print("copyrecord is running")# This method copies the specified row of data
    # from the source csv file to a destination file
    fields = []
    rows = []
    with open(input_file, 'r') as f1, open("/Users/danballard/Desktop/bar.csv", 'a') as f2 :
     #   line = f1.readline() #remove header
        line = f1.readline()
        print(line[2])
        while line[1] != 'Machine Sn':
            f2.write(line)
            line = f1.readline()



def readcsvfile (input_file):

    csv_data = csv.reader(open(input_file))

    # header_list will contain the line numbers for
    # the first header row in csv_data file.
    line_count = 0
    header_list = []
    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open(input_file, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)
        #print(fields)  #print the first header row
        #line_count=line_count + 1
        # extracting each data row one by one

        for row in csvreader:
            #rows.append(row)
            #print(row)              #print the entire row
            #print(row[0])           #print specified column data in that row
            if line_count == 0:
                #print(f' Column names are {",".join(row)}')
                line_count = line_count + 1
                header_list.append(line_count)
            else:
                #print(row)
                line_count = line_count + 1
                if row[0] == 'Machine Sn':
                    header_list.append(line_count)
                    #print("line_number:%d" % line_count)
                    #print(row)
                #line_number = line_count + 1
    # get total number of rows

        last_row = csvreader.line_num
        #print("$$$$header_list:%s" % header_list)
        #print("last row is:%d" % last_row)
        #add last row to the header_list
        #header_list.append(last_row)
        print("end of readcsvfile")
    return header_list
# printing the field names
#print('Field names are:' + ', '.join(field for field in fields))

def readfirstframe(input_file, header_list):
    end_row = header_list[1]
    csv_data = csv.reader(open(input_file))
    line_count = 0
    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open('/Users/danballard/Desktop/2111190013.csv', 'r') as csvfile, open('/Users/danballard/Desktop/bat.csv', 'a') as csvfileout:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        print(fields)  # print the first header row
        csvfileout.write(', '.join(map(str, fields)))
        for row in csvreader:
            if line_count == 0:
                print(f' Column names are {",".join(row)}')
                column_names = ','.join(map(str, row))
                csvfileout.write(column_names)
                csvfileout.write('\n')
                line_count = line_count + 1
            else:
                if line_count < end_row-1:
                        print(row)
                        csvfileout.write(','.join(map(str, row)))
                        csvfileout.write('\n')
                        line_count = line_count + 1

        # remove first entry in header list we are through with it.
        header_list.pop(0)
        print("end of readfirstframe")
    return header_list

def readcsvframes (input_file, header_list):
    print ("readcsvframes header list:%s" % header_list)


    #get next start address and end address from the header list
    # if there is only one entry in the header list then this is
    # the last dataframe and the end
    start_row= header_list.pop(0)
    end_row = header_list.pop(0)
    print("start_row:%d" % start_row)
    print ("end_row:%d" % end_row)
    csv_data = csv.reader(open(input_file))
    line_count = start_row
    # initializing the titles and rows list
    fields = []
    rows = []

    # reading csv file
    with open('/Users/danballard/Desktop/2111190013.csv', 'r') as csvfile, open('/Users/danballard/Desktop/batout.csv', 'a') as csvfileout:
            # creating a csv reader object
        csvreader = csv.reader(csvfile)
        print(csvfile.readlines())

        # extracting field names through first row
        #fields = next(csvreader)
        #print(fields)  # print the first header row
        #csvfileout.write(', '.join(map(str, fields)))
        for row in csvreader:
            # print('/n')
                #if line_count < start_row:
                #print(f' Column names are {",".join(row)}')
                #column_names = ','.join(map(str, row))
                #csvfileout.write(column_names)
                #csvfileout.write('\n')
                #next(csvreader)
                #line_count = line_count + 1
            #elif line_count >= start_row and line_count < end_row-1:
                #print(row)
                #csvfileout.write(','.join(map(str, row)))
                #csvfileout.write('\n')
                #next(csvreader)
                #line_count = line_count + 1
        #print ("end of readcvsframe")
        #return
            return

input_file = '/Users/danballard/Desktop/2111190013.csv'
output_file = '/Users/danballard/Desktop/bar.csv'
header_list =readcsvfile(input_file)
print(header_list)
start_row= header_list.pop(0)
#print(pd.read_csv(input_file, index_col=1, nrows=1).columns.tolist())
df1 = pd.read_csv(input_file)
#list_size = len(df1)
#print("list_size:%d" % list_size)
#while start_row < list_size-2:
    #print("####start_row:%d" % start_row)
    #end_row = header_list.pop(0)
    #print("####end_row:%d" % end_row)
    #df2 = df1.iloc[start_row:end_row-1, :]
    #print(df1.head())  # make the csv file here
    #xdate = df2.iloc[start_row:start_row, 5:]
    #print (xdate)
    #start_row = end_row
    #print("@@@@@start_row:%d" % start_row)

#print(df1)

df2 =df1.iloc[252:800,: ]
print(df2)