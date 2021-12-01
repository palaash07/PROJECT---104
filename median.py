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
# sorting of data
newdata.sort()
if n%2 == 0:
    median1 = float(newdata[n//2])
    median2 = float(newdata[n//2-1])
    median = (median1+median2)/2

else:
    median = newdata[n//2] 

print("median=",str(median))
