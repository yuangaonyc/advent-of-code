import pandas as pd
import sys

data = open("d8.txt").read().split("\n")

set_row = 6
set_col = 50

df = pd.DataFrame(data=0, index=list(range(0,set_row)), columns=list(range(0,set_col)))

def rect(cols, rows):
	df.iloc[:rows, :cols] = 1

def rotate_col(col, x):
	df_temp = df.copy()
	for i in range(0, set_row):
		df.iloc[i, col] = df_temp.iloc[i-x, col]

def rotate_row(row, x):
	df_temp = df.copy()
	for i in range(0, set_col):
		df.iloc[row, i] = df_temp.iloc[row, i-x]

for row in data:
	items = row.split(" ")
	if items[0] == "rect":
		rect(int(items[-1].split("x")[0]), int(items[-1].split("x")[-1]))

	elif items[1] == "row":
		rotate_row(int(items[2].split("=")[-1]), int(items[-1]))

	elif items[1] == "column":
		rotate_col(int(items[2].split("=")[-1]), int(items[-1]))

	else:
		print("something")

for i in range(0, set_row):
	for j in range(0, set_col):
		if df[j][i] == 0:
			sys.stdout.write('.')
		if df[j][i] == 1:
			sys.stdout.write('#')
	sys.stdout.write('\n')
