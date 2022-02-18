# importing csv module
import csv


# csv file name
filename = '/Users/danballard/Desktop/'+'2111190013.csv'

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)
    real_date = fields[5]
    print(real_date)



with open("filename.csv", r) as f1, open("/Users/danballard/Desktop/bar.csv", 'a') as f2 :
    line = f1.readline() #remove header
    line = f1.readline()
    while line != "" :
        f2.write(line)
        line = f1.readline()








































































































