'''
Created on Jun 22, 2016

@author: scntax
'''

import csv
import datetime

cr = csv.reader(open('anxhkAUD.csv', 'rb'))

print "time", "price", "amount"

for row in cr:
    print (datetime.datetime.fromtimestamp(int(row[0])).strftime('%Y-%m-%d %H:%M:%S')), row[1], row[2]


'''
print(
    datetime.datetime.fromtimestamp(
        int(row[0])
    ).strftime('%Y-%m-%d %H:%M:%S')
)
'''