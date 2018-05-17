from parse import parse
from parse import write_back
import math
import sys

def correct_height(list): # Correct height to inches
    for i in range(len(list)):
        ft, inch = list[i]["Ht"].split("-")
        list[i]["Ht"] = (int(ft)*12) + int(inch)

def normalize_stat(list, stat): # stat is a string
    max = 0
    min = sys.maxint
    for i in range(len(list)): # find the min and max values
        if list[i][stat] != "":
            list[i][stat] = float(list[i][stat])
            if list[i][stat] < min:
                min = list[i][stat]
            if list[i][stat] > max:
                max = list[i][stat]
        else:
            list[i][stat] = "?"
    range_val = max - min
    print range_val
    for j in range(len(list)):
        if list[j][stat] != "?":
            list[j][stat] = float(list[j][stat]-min) / float(range_val)

def normalize_stat_list(data, stats):
    for i in range(len(stats)):
        normalize_stat(data, stats[i])


# TODO Add question marks to all columns
def fix_names(list): # TODO Check this!!!!
    for i in range(len(list)):
        for char in list[i]["Player"]:
            if char in "'":
                list[i]["Player"].replace(char,'')


# Extract just the round from the last column




# Parse returns a list of dictionaries
features_to_normalize = ["Ht", "Wt", "40yd", "Vertical", "Bench", "Broad Jump", "3Cone", "Shuttle"]
comb2018 = parse ("combine2018.csv")
correct_height(comb2018)
fix_names(comb2018)
normalize_stat_list(comb2018, features_to_normalize)
write_back("test_out.csv", comb2018)
