import sys

# sys argv returns the argument to the program
def main():
# saves the arguement to the variable
    filename =sys.argv[1]
    read_file(filename)
# function reads the file and
## puts data in a list filled with tuples
# tuples have the required format
def read_file(filename):
    log_file = open(filename, 'r')
    list_tuples = []
    end = False
    while not end:
        name = log_file.readline()
        if not name:
            end = True
        else:
            list_tuples.append((name,log_file.readline()))
    log_file.close()
    return list_tuples



def display_entry(name, message):
    

    print(name, message)




main()