import math
import sys


def read_lines(filename):
    try:
        log_file = open(filename, 'r')
    except:
        print(f"An error occurred while trying to read the file.")
        exit()
    end = False
    list_of_strings = []
    while not end:
        name = log_file.readline()
        if not name:
            end = True
        else:
            list_of_strings.append(name.replace('\n', ''))
    log_file.close()
    return list_of_strings


def parse_cars(list_of_strings):
    cars = []
    for strings in list_of_strings:
        new_data = strings.split(":")
        cars.append((new_data[0], int(new_data[1])))
    return cars


def calculate_percentage(distance, cars):
    percentages = []
    for car in cars:
        car_percent = float(distance / car[1] * 100)
        percentages.append((car[0], car_percent))
    return percentages


def display_result(percentages):
    print("\n\nTo drive the specified distance would correspond to this many\n"
          "percent of each cars specified max range.")
    for percentage in percentages:
        # saving percentage in variable to do if
        car_percent = round(percentage[1])
        if car_percent > 100:
            print(f"{percentage[0]:36} -->  Distance exceeds max range ({car_percent}%)")
        else:
            print(f"{percentage[0]:36} -->  {car_percent}%")


def main():
    filename = sys.argv[1]
    list_of_strings = read_lines(filename)
    cars = parse_cars(list_of_strings)
    input_distance = int(input("How far do you want to drive (kilometers)?"))
    percentages = calculate_percentage(input_distance, cars)
    display_result(percentages)


if __name__ == '__main__':
    main()
