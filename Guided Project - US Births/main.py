from us_births import *
from helpers import *

#Reading csv files into lists
cdc_list = read_csv("data/US_births_1994-2003_CDC_NCHS.csv")
ssa_list = read_csv("data/US_births_2000-2014_SSA.csv")

#final_list = merge_births_average(cdc_list,ssa_list)
print(merge_births_lists(cdc_list,ssa_list))
