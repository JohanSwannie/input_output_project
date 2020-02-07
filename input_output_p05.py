import csv

with open('swannie1.csv') as csv1f:
	csv1 = csv.reader(csv1f, delimiter=":")
	line_cnt = 0
	for row in csv1:
		if line_cnt == 0:
			print(f"The Columns for this request are {', '.join(row)}")
			line_cnt += 1
		else:
			print(f"{row[0]} works in the {row[1]} department, and was born on {row[2]} and lives in {row[3]}.")
			line_cnt += 1
	print(f"This request has processed {line_cnt} lines")

import csv

with open('swannie2.csv') as csv2f:
	csv2 = csv.DictReader(csv2f)
	line_cnt = 0
	for row in csv2:
		print(row)
		if line_cnt == 0:
			print(f"The Columns for this request are {', '.join(row)}")
			line_cnt += 1
		else:
			print(f"{row[0]} with surname {row[1]} has a hobby of {row[2]} and lives in {row[3]}.")
			line_cnt += 1
	print(f"This request has processed {line_cnt} lines")

import pandas

df = pandas.read_csv('swannie2.csv')

df_2 = pandas.read_csv('swannie2.csv', index_col='Name')

df_3 = pandas.read_csv('swannie2.csv', index_col='Name', parse_dates=['Hire Date'])

df_4 = pandas.read_csv(
	'swannie2.csv',
	index_col='Employee',
	parse_dates=['Hired'],
	header=0,
	names=['Employee', 'Hired', 'Salary', 'Leave Days']
)

print(df_4)
