#!/usr/bin/python3

import csv
with open ('query.csv' , newline='') as csvfile:
  queryreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in queryreader:
    print(', '.join(row))

