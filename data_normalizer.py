from parse import parse
from parse import write_back
import math
import sys
import os
import re

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
    for j in range(len(list)):
        if list[j][stat] != "?":
            list[j][stat] = float(list[j][stat]-min) / float(range_val)

def normalize_stat_list(data, stats):
    for i in range(len(stats)):
        normalize_stat(data, stats[i])


# TODO Add question marks to all columns
def fix_names(list): # TODO Check this!!!!
    for i in range(len(list)):
        list[i]["Player"] = list[i]["Player"].replace("'", "")
        if list[i]["Drafted (tm/rnd/yr)"] != "":
            list[i]["Drafted (tm/rnd/yr)"] = re.split(' / ', list[i]["Drafted (tm/rnd/yr)"])[1]
        else:
            list[i]["Drafted (tm/rnd/yr)"] = 0
        print list[i]["Drafted (tm/rnd/yr)"]

def listdir_nohidden(path):
    f = os.listdir(path)
    to_delete = []
    for i in range(len(f)):
        if ".D" in f[i]:
            to_delete.append(f[i])
    for j in to_delete:
        f.remove(j)
    return f

def main():
    files_to_normalize = listdir_nohidden('./csv_to_parse')
    features_to_normalize = ["Ht", "Wt", "40yd", "Vertical", "Bench", "Broad Jump", "3Cone", "Shuttle"]
    for i in range(len(files_to_normalize)):
        comb_stats = parse("./csv_to_parse/"+files_to_normalize[i])
        correct_height(comb_stats)
        fix_names(comb_stats)
        normalize_stat_list(comb_stats, features_to_normalize)
        write_back("./new_csv/"+files_to_normalize[i], comb_stats)

if __name__ == '__main__':
    main()
