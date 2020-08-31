from csv import reader
from math import sqrt
from random import seed
from random import randrange

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

def print_first_rows(dataset, rows=10):
	for i in range(rows):
		print(dataset[i])

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

# Find the min and max values for each column
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

# calculate column means
def column_means(dataset):
	means = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		means[i] = sum(col_values) / float(len(dataset))
	return means

# calculate column standard deviations
def column_stdevs(dataset, means):
	stdevs = [0 for i in range(len(dataset[0]))]
	for i in range(len(dataset[0])):
		variance = [pow(row[i]-means[i], 2) for row in dataset]
		stdevs[i] = sqrt(sum(variance)/(float(len(dataset)-1)))
	return stdevs

# standardize dataset
def standardize_dataset(dataset, means, stdevs):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - means[i]) / stdevs[i]

# Split a dataset into a train and test set
def train_test_split(dataset, split=0.60):
	train = list()
	train_size = split * len(dataset)
	dataset_copy = list(dataset)
	while len(train) < train_size:
		index = randrange(len(dataset_copy))
		train.append(dataset_copy.pop(index))
	return train, dataset_copy

#--------------------------------------------------
dataset = load_csv("wine.data")
print_first_rows(dataset)

for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)

minmax = dataset_minmax(dataset)
print(minmax)

means = column_means(dataset)
stdevs = column_stdevs(dataset, means)
print(means)
print(stdevs)
print("")

dataset1 = dataset.copy()
normalize_dataset(dataset1, minmax)
print_first_rows(dataset1)
print("")

dataset2 = dataset.copy()
standardize_dataset(dataset2, means, stdevs)
print_first_rows(dataset2)
print("")

train, test = train_test_split(dataset)
print_first_rows(train)
print("")
print_first_rows(test)
print("")