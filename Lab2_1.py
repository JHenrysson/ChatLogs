import sys


# sys argv returns the CL argument
def main():
    # saves the argument to the variable
    filename = sys.argv[1]
    #calling function readfile and saving the return value to the variable
    list_of_tuples = read_file(filename)
    user_input = input("Enter a name to search for: ")
    # tuple is an item of the tuples with name,message
    for tuple in list_of_tuples:
        # the name is in index 0
        name_in_tuple = tuple[0]
        if name_in_tuple == user_input:
            print(display_entry(name_in_tuple, tuple[1]))


# function reads the file and
# puts data in tuples the tuple contains name and message
def read_file(filename):
    try:
        log_file = open(filename, 'r')
    except:
        #if the file is not valid then this message will be printed
        print(f"Error: The file '{filename}' could not be found.")
        exit()
    list_tuples = []
    # end is used to check if we have reached the end of the file
    end = False
    # loops until the end of the file
    while not end:
        #reads the next line in the file
        name = log_file.readline()
        if not name:
            # the end of the file is reached
            # set end to true so that the loop does not continue
            end = True
        else:
            #adding the name into a tuple without the line break
            #reads the next line containing the message w/o line break adding to tuple
            # adds tuple to the list of tuples
            list_tuples.append((name.replace('\n', ''), log_file.readline().replace('\n', '')))
    log_file.close()
    return list_tuples

# the function used to display both the name and message - returns a formatted value
def display_entry(name, message):
    return f"[{name}] --> {message}"


if __name__ == '__main__':
    main()
