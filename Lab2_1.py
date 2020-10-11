import sys

# sys argv returns the argument to the program
def main():
# saves the argument to the variable
    filename = sys.argv[1]
    list_of_tuples=read_file(filename)
    user_input = input("Enter a name to search for: ")
    # tuple is an item of the tuple with name,message
    for tuple in list_of_tuples:
        name_in_tuple = tuple[0]
        if name_in_tuple == user_input:
            display_entry(name_in_tuple, tuple[1])

# function reads the file and
## puts data in tuples -- tuple contain name and message
def read_file(filename):
    try:
        log_file = open(filename, 'r')
    except:
        exit(f"Error: The file '{filename}' could not be found.")
    list_tuples = []
    end = False
    while not end:
        name = log_file.readline()
        if not name:
            end = True
        else:
            list_tuples.append((name.replace('\n',''),log_file.readline().replace('\n','')))
    log_file.close()
    return list_tuples

def display_entry(name,message):
    print(f"[{name}] --> {message}")



main()