## Takes in csv file and isolates round in Drafted attribute
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
