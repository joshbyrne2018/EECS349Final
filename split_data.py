# split combine data into training data and holdout data
import random


def split(inFile):
    fin = open(inFile, 'rb')
    header = fin.readline()
    data = fin.readlines()[1:]
    random.shuffle(data)

    f_train_out = open("./new_training_and_holdout_data/new_combine_training_data.csv", 'wb')
    f_holdout_out = open("./new_training_and_holdout_data/new_combine_holdout_data.csv", 'wb')
    f_train_out.write(header)
    f_holdout_out.write(header)

    nLines = len(data)
    nTrain = nLines * 0.75
    nHoldout = nLines - nTrain

    i = 0
    for line in data:
        r = random.random()
        if (i < nTrain and r < 0.75) or (nLines - i > nHoldout):
            f_train_out.write(line)
            i += 1
        else:
            f_holdout_out.write(line)


if __name__ == '__main__':
    split("./interact_csv/combined_stats_binary_with_interaction_attributes.csv")