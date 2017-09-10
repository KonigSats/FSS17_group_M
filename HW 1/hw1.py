from multiprocessing import Queue
import sys


def process_header(line,header):
	try:
		comment_loc = line.index("#")   #detect the comments
	except:
		comment_loc = len(line)
	line = line[0:comment_loc]			#eliminate the comments
	for x in line.split(','):			#split using delimiter
		x = x.strip()					#remove whitespaces
		if x!= "":
			header.append(x)

def process_data_and_enqueue(line,table,j):
	try:
		comment_loc = line.index("#")   #detect the comments
	except:
		comment_loc = len(line)
	line = line[0:comment_loc]			#eliminate the comments
	for x in line.split(','):			#split using delimiter
		x = x.strip()					#remove whitespaces
		if x!= "":
			table[j%column_numbers].append(x)
			j=j+1

q = []
input = open(sys.argv[1], 'rb')
line = input.readline()
header = []
process_header(line,header)
table=[]
for element in header:
	minitable=[]
	minitable.append(element)
	table.append(minitable)
	
column_numbers=len(header)

#print(header)

line = input.readline()
j=0
while line:
	process_data_and_enqueue(line,table,j)
	line = input.readline()

for column in table:
	print(column)
