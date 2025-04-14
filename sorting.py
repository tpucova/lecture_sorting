import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        data = csv.DictReader(csv_file)
        for row in data:
            print(row)
    return data

def selection_sorting(list_of_numbers):
    for idx in range(len(list_of_numbers)):
        min_idx = idx
        for idx_new in range(idx + 1, len(list_of_numbers)):
            if list_of_numbers[idx_new] < list_of_numbers[min_idx]:
                min_idx = idx_new
        list_of_numbers[idx], list_of_numbers[min_idx] = list_of_numbers[min_idx], list_of_numbers[idx]
    return list_of_numbers

def bubble_sort(sequence):
    for idx in range(len(sequence) - 1):
        for idx_new in range(len(sequence) - idx - 1):
            if sequence[idx_new] > sequence[idx_new + 1]:
                sequence[idx_new + 1], sequence[idx_new] = sequence[idx_new], sequence[idx_new + 1]
    return sequence

def insertion_sort(sequence):
    for idx in range(1, len(sequence)):
        value = sequence[idx]
        j = idx - 1
        while (sequence[j] > value) and (j >= 0):
            sequence[j + 1] = sequence[j]
            j = j - 1
        sequence[j + 1] = value
    return sequence

def main():
    my_data = read_data('numbers.csv')
    print(my_data)
    sorted_list = selection_sorting([2,5,1,3,8,45,12,4])
    print(sorted_list)
    print(bubble_sort([85,45,49,25,68]))
    print(insertion_sort([9, 5, 1, 4, 3]))


if __name__ == '__main__':
    main()
