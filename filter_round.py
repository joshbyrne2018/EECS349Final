## Takes in csv file and isolates round in Drafted attribute
## writes over infile
def filter_round(infile):
    lines = []
    row = []
    draft = []
    newline = ""
    f = open(infile, "r")
    headers = f.readline()
    ln = f.readline()
    while ln:
        newline = ""
        row = ln.split(',')
        draft = row[len(row)-1].split('/')
        if len(draft) == 1:
            round = "0"
        else:
            round = draft[1].strip(' ')
        for i in range(0,len(row)-1):
            newline += row[i] + ','
        newline += round + '\n'
        lines.append(newline)
        ln = f.readline()

    f.close()
    fout = open(infile, "w")
    fout.write(headers)

    for line in lines:
        fout.writelines(line)

    fout.close()

def drafted_or_not(infile,outfile):
    lines = []
    row = []
    draft = []
    newline = ""
    f = open(infile, "r")
    headers = f.readline()
    ln = f.readline()
    while ln:
        newline = ""
        row = ln.split(',')
        draft = row[len(row)-1]
        if '0' not in draft:
            round = "1"
        else:
            round = draft
        for i in range(0,len(row)-1):
            newline += row[i] + ','
        newline += round + '\n'
        lines.append(newline)
        ln = f.readline()

    f.close()
    fout = open(outfile, "w")
    fout.write(headers)

    for line in lines:
        fout.writelines(line)

    fout.close()
drafted_or_not("combine_training_data.csv", "combine_training_binary.csv")
