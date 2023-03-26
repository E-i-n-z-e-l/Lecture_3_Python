# Функции

def sum_numbers(n):
	summa = 0
	for i in range(1, n + 1):
		summa = summa + i
	print(summa)

sum_numbers(5)


# Функции позволяют передавать неограниченное кол-во элементов

def sum_str(*args):
	res = ''
	for i in args:
		res = res + i
	return res

print(sum_str('a', 'b', 'c'))


# Модули

# Импортировать модуль: import (тут пишем фаил в котором хранятся функции)
# 		      from (названия фаила) import * - импортировать все функции в модули (вместо звездочки можно указать конкретную функцию)


# Пример:

# print(название модуля.название функции(данные для функции))


# Рекурсия!!!

# Числа Фибоначчи

def fib(n):
	
	if n in [1, 2]:
		
		return 1
	
	return fib(n - 1) + fib(n - 2)

list_1 = []

for i in range(1, 10):
  
	list_1.append(fib(i))


print(list_1) 


# Сортировка с помощью рекурсии

def quicksort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [i for i in array[1:] if i > pivot]
		return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

# 1-е повторение рекурсии:
# 0 array = [10, 5, 2, 3]
# 0 pivot = 10
# 0 less = [5, 2, 3]
# 0 greater = []
# 0 return quicksort([5, 2, 3]) + [10] + quicksort([])

# 2-е повторение рекурсии:
# 0 array = [5, 2, 3]
# 0 pivot = 5
# 0 less = [2, 3]
# 0 greater = []
# 0 return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что
# здесь помимо вызова рекурсии добавляется список [10]

# 3-е повторение рекурсии:
# 0 array = [2, 3]
# 0 return [2, 3] # Сработал базовый случай рекурсии

# На этом работа рекурсии завершилась и итоговый список будет выглядеть таким
# образом: [2, 3] + [5] + [10] = [2, 3, 5, 10]


# Сортировка слиянием

def merge_sort(nums):
	if len(nums) > 1:
		mid = len(nums) // 2
		left = nums[:mid]
		right = nums[mid:]
		merge_sort(left)
		merge_sort(right)
		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				nums[k] = left[i]
				i += 1
			else:
				nums[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			nums[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			nums[k] = right[j]
			j += 1
			k += 1

nums = [38, 27, 43, 3, 9, 82, 10]
merge_sort(nums)
print(nums)

