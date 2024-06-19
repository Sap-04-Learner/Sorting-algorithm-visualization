import time

# sorting algorithm
# bubble sort
def bubble_sort(arr):
	n = len(arr)
	swapped = True
	while swapped:
		time.sleep(0.01)
		swapped = False
		for i in range(len(arr)-1):
			time.sleep(0.01)
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
				swapped = True

	return arr

# selection sort
def selection_sort(arr):
	n = len(arr)
	for i in range(n):
		time.sleep(0.01)
		min_idx = i
		for j in range(i+1, n):
			time.sleep(0.01)
			if arr[j] < arr[min_idx]:
				time.sleep(0.01)
				min_idx = j
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
		time.sleep(0.01)

	return arr

# insertion sort
def insertion_sort(arr):
	n = len(arr)
	for i in range(1, n):
		time.sleep(0.01)
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			time.sleep(0.01)
			arr[j + 1] = arr[j]
			j -= 1		
		arr[j + 1] = key
	
	return arr

# merge sorting
def merge_sort(arr):
	if len(arr) > 1:
		time.sleep(0.01)
		mid = len(arr) // 2

		left_half = arr[:mid]
		time.sleep(0.01)
		right_half = arr[mid:]
		time.sleep(0.01)

		time.sleep(0.01)
		merge_sort(left_half)
		time.sleep(0.01)
		merge_sort(right_half)

		i = j = k = 0
		while i < len(left_half) and j < len(right_half):
			time.sleep(0.01)
			if left_half[i] < right_half[j]:
				arr[k] = left_half[i]
				i += 1
			else:
				arr[k] = right_half[j]
				j += 1
			k += 1

		while i < len(left_half):
			time.sleep(0.01)
			arr[k] = left_half[i]
			i += 1
			k += 1
		while j < len(right_half):
			time.sleep(0.01)
			arr[k] = right_half[j]
			j += 1
			k += 1

	return arr

# quick sorting
def quick_sort(arr):
	def partition(low, high):
		pivot = arr[high]
		i = low - 1
		for j in range(low, high):
			time.sleep(0.01)
			if arr[j] <= pivot:
				i += 1
				arr[i], arr[j] = arr[j], arr[i]
		arr[i + 1], arr[high] = arr[high], arr[i + 1]
		return i + 1
	
	def _quick_sort(low, high):
		if low < high:
			time.sleep(0.01)
			pi = partition(low, high)
			time.sleep(0.01)
			_quick_sort(low, pi - 1)
			time.sleep(0.01)
			_quick_sort(pi + 1, high)
	
	_quick_sort(0, len(arr) - 1)

	return arr
