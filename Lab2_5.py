import sys


def read_file(filename):
    try:
        log_file = open(filename, 'r')
    except:
        print(f"An error occurred while trying to read the file.")
        exit()
    end = False
    list_of_numbers = []
    while not end:
        row = log_file.readline()
        if not row:
            end = True
        else:
            row_without_new_line = row.replace('\n', '')
            number_array = row_without_new_line.split(' ')
            for number in number_array:
                list_of_numbers.append(int(number))

    log_file.close()
    return list_of_numbers


# returns list

def filter_odd_or_even(numbers, odd):
    # empty filter list
    filter_list = []
    # for loop going through the list
    for x in numbers:
        # even numbers divided by 2 should not have a reminder
        number_even = x % 2 == 0
        # filter even numbers but adding odd (odd is sent in from main)
        if odd and not number_even:
            filter_list.append(x)
        # filter odd numbers but adding even
        elif not odd and number_even:
            filter_list.append(x)
    return filter_list


def reversed_bubble_sort(numbers):
    # number of times it will loop through the list
    for i in range(0, len(numbers)):
        # looping through list and switching list items based on value
        for x in range(0, len(numbers) - 1):
            if numbers[x] < numbers[x + 1]:
                # switches values
                numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]


def main():
    # sys argv returns the CL argument 1st / 2nd
    list_one = read_file(sys.argv[1])
    list_two = read_file(sys.argv[2])
    list_odd = filter_odd_or_even(list_one, True)
    list_even = filter_odd_or_even(list_two, False)
    combined_lists = list_even + list_odd
    reversed_bubble_sort(combined_lists)
    print(combined_lists)
if __name__ == '__main__':
    main()
