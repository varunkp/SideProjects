import csv

with open('phonenumbers.csv', 'rb') as csvfile:
	numberreader = csv.reader(csvfile, delimiter = '\n')