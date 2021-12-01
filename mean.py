import csv
with open("SOCR-HeightWeight.csv",newline='')as f:
    df = csv.reader(f)
    filedata = list(df)

# removing title names

filedata.pop(0)
#fetching all the heights only in a variable 

newdata = []
for i in range(len(filedata)):
    num = filedata[i][1]
    newdata.append(float(num))

#calculating lenght of the height 

n = len(newdata)
# sum of all the items of new data 
total = 0
for i in newdata :
    total = total+i 

# calculating mean 
mean = total/n

print("mean = "+str(mean))
