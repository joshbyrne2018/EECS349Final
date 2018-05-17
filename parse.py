import csv

def parse(filename):
  '''
  takes a filename and returns attribute information and all the data in array of dictionaries
  '''
  # initialize variables

  out = []
  csvfile = open(filename,'rb')
  fileToRead = csv.reader(csvfile)

  headers = fileToRead.next()

  # iterate through rows of actual data
  for row in fileToRead:
    out.append(dict(zip(headers, row)))

  return out

def write_back(filename, list):
    f = open(filename,'wb')
    w = csv.writer(f)
    w.writerow(list[0].keys())
    for i in range(len(list)):
        w.writerow(list[i].values())
    f.close()
