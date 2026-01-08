__title__ = "Coding activity 2, psuedocode to code"
__author__ = "John Rodgers"

numbers = [10, 2, 4, 3, 5, 6, 8, 7, 1, 9]

def sort_and_find_median(numbers):
    sort(numbers)
    n = len(numbers)
    if n % 2 == 0:
        return (numbers[n//2 -1] + numbers[n//2])/2
    else:
        return numbers[n//2]
# find median of list

def sort(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# bubble sort list in ascending order

median = sort_and_find_median(numbers)
print(numbers)
print(median)
# output

