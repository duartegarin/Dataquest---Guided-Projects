# Function that reads our csv and structures the data
def read_csv(file_name):
    #Opening our births file
    file = open(file_name,"r")
    file_contents = file.read()

    #Structuring our file
    file_rows = file_contents.split("\n")
    string_list = file_rows[1:len(file_rows)]

    #Looping through each row, splitting the values, transform then to ints and creating a list of lists with treated values
    final_list = []
    for list_item in string_list:
        int_fields = []

        string_fields = list_item.split(",")
        for field in string_fields:
            int_fields.append(int(field))

        final_list.append(int_fields)

    return final_list
def minmax(dictionary,minmax):
    if minmax == "max":
        return dictionary[max(dictionary,key=dictionary.get)]
    elif minmax == "min":
        return dictionary[min(dictionary,key=dictionary.get)]
