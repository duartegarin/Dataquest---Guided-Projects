# Function that calculates the number of births per month
def month_births(list):
    births_per_month = {}
    for entry in list:
        month = entry[1]
        births = entry[4]
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return births_per_month
# Function that returns the number of births per day of week
def dow_births(list):
    births_per_dow = {}
    for entry in list:
        dow = entry[3]
        births = entry[4]
        if dow in births_per_dow:
            births_per_dow[dow] += births
        else:
            births_per_dow[dow] = births
    return births_per_dow
# Generic birth query function
def calc_counts(data,column):
    births_per_column = {}
    for entry in data:
        attribute = entry[column]
        births = entry[4]
        if attribute in births_per_column:
            births_per_column[attribute] += births
        else:
            births_per_column[attribute] = births
    return births_per_column
def calc_counts2(data,column,column_consecutive_value):
    births = {}
    for element in data:
        if element[0] in births and element[column] == column_consecutive_value:
            births[element[0]] += element[4]
        elif element[0] not in births and element[column] == column_consecutive_value:
            births[element[0]] = element[4]
    cdc_year_births = births
    return(cdc_year_births)
def merge_births_average(list1,list2):

    #These lists will be clones of the original lists without the last column (births)
    truncated_list_1 = []
    truncated_list_2 = []

    #Here we fill in the truncated lists with each item of the original lists minus the last column
    for item in list1:
       truncated_list_1.append(item[0:len(item)-1])
    for item in list2:
       truncated_list_2.append(item[0:len(item)-1])

    for item in list1:

        #Now the find will work as we can apply exact matches between our truncated lists
        if [item[0],item[1],item[2],item[3]] in truncated_list_2:

            #If we find a match we need to know the index in both lists so we can do an average
            index1 = truncated_list_1.index([item[0],item[1],item[2],item[3]])
            index2 = truncated_list_2.index([item[0],item[1],item[2],item[3]])

            #For convenience I am adding the average in list1
            list1[index1][4] += list2[index2][4]/2

    return list1
def merge_births_lists(list1,list2):

    catalog = {}

    for each in list1:

        year = each[0]
        month = each[1]
        date_of_month = each[2]
        day_of_week = each[3]
        births = each[4]

        catalog[(year,month,date_of_month,day_of_week)] = births
    for each in list2:

        year = each[0]
        month = each[1]
        date_of_month = each[2]
        day_of_week = each[3]
        births = each[4]

        if (year,month,date_of_month,day_of_week) in catalog:
             catalog[(year,month,date_of_month,day_of_week)] = (catalog[(year,month,date_of_month,day_of_week)] + births)/2
    final_list = []
    for key in catalog.keys():
        year = key[0]
        month = key[1]
        date_of_month = key[2]
        day_of_week = key[3]
        final_list.append([year,month,date_of_month,day_of_week,catalog[key]])

    return final_list
