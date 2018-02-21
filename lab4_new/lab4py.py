import pandas as pd
import numpy as np
import random
df = pd.read_csv("jester-data-1.csv")
df = df.head(n=10)
df_copy = df.copy()
# print "687900"
count = 0
# print "counting"
# for index, row in df.iterrows():
#     print index
#     print row[0]
#
#     print df.iat[index,0]

while(count < 183528):
    print "in"
    # print "count", count
    for index, row in df.iterrows():
        for i in range(2):
            rc = random.randint(0,100)
            if (row[rc] != 99 and count < 183528):
                df_copy.iat[index, rc] = 99
                count = count + 1

print "count", count


count = 0
for index, row in df_copy.iterrows():
    for i in row:
        if(i == 99):
            count = count + 1
print count

count = 0
for index, row in df_copy.iterrows():
    for i in row:
        if(i == 99):
            count = count + 1
print count
# print (687900.00/2523182.00)
#
# print (100 - (687900.00/2523182.00)*100)
# print ((100 - (687900.00/2523182.00)*100) * 2523182)/100



# 27.

# 1835282

