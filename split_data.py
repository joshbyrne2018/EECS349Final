# split combine data into training data and holdout data
import random


def split():
    fin = open("./merged_csv/combine2008-2018.csv", 'rb')
    f_train_out = open("./training_and_holdout_data/combine_training_data", 'wb')
    f_holdout_out = open("./training_and_holdout_data/combine_holdout_data", 'wb')
    f_holdout_out.write("School,Vertical,3Cone,Pos,Ht,Bench,Player,Broad Jump,Wt,College,40yd,Shuttle,Drafted (tm/rnd/yr)\n")

    nLines = sum(1 for line in fin)
    fin.seek(0)
    nTrain = int(nLines * 0.75)
    nHoldout = nLines - nTrain

    i = 0
    for line in fin:
        r = random.random()
        if (i < nTrain and r < 0.75) or (nLines - i > nHoldout):
            f_train_out.write(line)
            i += 1
        else:
            f_holdout_out.write(line)


if __name__ == '__main__':
    split()