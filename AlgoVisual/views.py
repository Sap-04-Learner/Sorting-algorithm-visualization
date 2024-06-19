from django.shortcuts import render
import csv
from . import sort_algo as sort
from . import multiProcess as mp
import random

# Create your views here.
def home(request):
	return render(request, 'home.html')

# to read from csv file
def read_csv(path):
	csv_file = path
	data = []
	with open(csv_file, 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			data.append([
				int(row['Size']),
				float(row['Best_case']),
				float(row['Average_case']),
				float(row['Worst_case'])
			])

	return data

def viewBubble(request):
	if request.method == 'POST' and request.POST.get('action') == 'start':
		mp.main('bubble')
		csv_file = 'static/bubblesort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'bubbleSort.html', {'data': data})
	else:
		csv_file = 'static/bubblesort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'bubbleSort.html', {'data': data})

def viewInsertion(request):
	if request.method == 'POST' and request.POST.get('action') == 'start':
		mp.main('insertion')
		csv_file = 'static/insertionsort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'insertionSort.html', {'data': data})
	else:
		csv_file = 'static/insertionsort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'insertionSort.html', {'data': data})

def viewSelection(request):
	if request.method == 'POST' and request.POST.get('action') == 'start':
		mp.main('selection')
		csv_file = 'static/selectionsort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'selectionSort.html', {'data': data})
	else:
		csv_file = 'static/selectionsort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'selectionSort.html', {'data': data})

def viewMerge(request):
	if request.method == 'POST' and request.POST.get('action') == 'start':
		mp.main('merge')
		csv_file = 'static/mergesort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'mergeSort.html', {'data': data})
	else:
		csv_file = 'static/mergesort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'mergeSort.html', {'data': data})

def viewQuick(request):
	if request.method == 'POST' and request.POST.get('action') == 'start':
		mp.main('quick')
		csv_file = 'static/quicksort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'quickSort.html', {'data': data})
	else:
		csv_file = 'static/quicksort_time_complexity.csv'
		data = read_csv(csv_file)
		return render(request, 'quickSort.html', {'data': data})

def viewCompare(request):
	csv_file = 'static/Algorithm_sorting_times.csv'
	data = []
	with open(csv_file, 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			data.append([
				int(row['Size']),
				float(row['Bubble Sort']),
				float(row['Selection Sort']),
				float(row['Insertion Sort']),
				float(row['Merge Sort']),
				float(row['Quick Sort']),
			])

	if request.method == 'POST':
		list_input = request.POST.get('list_input')
		array_sizes = request.POST.get('array_sizes')

		if list_input:  # If manual data input is provided
			input_list = [int(x) for x in list_input.split(',')]
			sorting_times = mp.sorting_performance_analysis(input_list)
			
			return render(request, 'compareAlgo.html', {'sorting_times': {
				'size' : len(input_list),
				'unsorted_list': input_list,
				'sorted_list' : sorted(input_list),
				'bubble_time': sorting_times[0],
				'selection_time': sorting_times[1],
				'insertion_time': sorting_times[2],
				'merge_time': sorting_times[3],
				'quick_time': sorting_times[4],
			}, 'data1': data})
		elif array_sizes:  # If array sizes are provided
			size = int(array_sizes)
			# Generate a random array of the specified size
			input_list = [random.randint(1, 1000) for _ in range(size)]
			# Call your Python function with the generated list
			sorting_times = mp.sorting_performance_analysis(input_list)
			
			return render(request, 'compareAlgo.html', {'sorting_times': {
				'size' : size,
				'unsorted_list': input_list,
				'sorted_list' : sorted(input_list),
				'bubble_time': sorting_times[0],
				'selection_time': sorting_times[1],
				'insertion_time': sorting_times[2],
				'merge_time': sorting_times[3],
				'quick_time': sorting_times[4],
			}, 'data1': data})
		else:
			return render(request, 'compareAlgo.html', {'data1': data})
	else:
		return render(request, 'compareAlgo.html', {'data1': data})
