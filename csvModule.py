#!/usr/bin/python3

import csv
with open ('query.csv' , newline='') as csvfile:
  queryreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in queryreader:
    print(', '.join(row))

with open ('query.csv', 'w', newline='') as csvfile:
  querywriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
  querywriter.writerrow(['Eleonora Debor'] * 5 + ['John Miller'])
  querywriter.writerrow(['Brad Poed', 'Stefan Drox'])
