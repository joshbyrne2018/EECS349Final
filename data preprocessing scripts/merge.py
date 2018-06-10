# merge all combine data into single csv
def merge():
    fout = open("./merged combine data/combine2008-2018.csv", "a")

    # first file:
    for line in open("./normalized combine data (original)/combine2008.csv"):
        fout.write(line)
    # remaining files:
    for num in range(2009, 2019):
        f = open("./normalized combine data (original)/combine" + str(num) + ".csv")
        f.next()  # skip the header
        for line in f:
            fout.write(line)
        f.close()
    fout.close()


if __name__ == '__main__':
    merge()