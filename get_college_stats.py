import requests
import bs4
import HTMLParser

def main():
    #get_college_stat_urls("https://www.pro-football-reference.com/draft/2018-combine.htm")
    get_stats_from_url("https://www.sports-reference.com/cfb/players/dante-pettis-1.html", "./college_stats/Dante_Pettis.csv")
    #uncomment_html("Dante_Pettis0.html", "DPUC.html")

def get_college_stat_urls(url):
    href = {}
    rows = []
    response = requests.get(url)
    bs = bs4.BeautifulSoup(response.text, 'html.parser')
    for r in bs.find_all('tr'):
        cs_link = "None"
        if 'csk' in str(r):
            rows.append(r)
        a = str(r.a)
        td_str = str(r.td)
        th_str = str(r.th)
        tr_bs = bs4.BeautifulSoup(str(r), 'html.parser')
        college_stat = tr_bs.find_all('a')
        for link in college_stat:
            if 'sports-reference' in str(link):
                cs_link = link.get('href')
                break
        if 'csk' in th_str:
            narr = th_str.split('"')[3].replace("'","").split(',')
            name = narr[1] + ' ' + narr[0]
            print name
            href[name] = cs_link
    # f = open("college_stat_href.txt", 'w+')
    # for h in href:
    #     strng = str(h) +': ' + str(href[h]) + '\n'
    #     f.writelines(strng)
    # f.close()

## Given url for college stats, find all the tables in the html and parse them into CSVs
def get_stats_from_url(url, outfile):
    fhtml_name = "./html/" + outfile[:len(outfile)-3].split('/')[len(outfile.split('/'))-1] + "html"
    u_name = fhtml_name[:len(fhtml_name)-5] + "_uncommented.html"
    fhtml = open(fhtml_name, 'w')
    response = requests.get(url)
    bs_st = bs4.BeautifulSoup(response.text, 'lxml').prettify().encode("utf-8")
    fhtml.write(bs_st)
    fhtml.close()
    uncomment_html(fhtml_name, u_name)
    uncom = open(u_name, 'r')
    commas = 0
    bs = bs4.BeautifulSoup(uncom.read(), 'lxml')
    uncom.close()
    tid = []
    fout = open(outfile, 'w')
    headers = ""
    stats = ""

    for cell in bs.find_all('td'):
        if cell.has_attr('data-stat'): headers += str(cell.get('data-stat')) + ','

    headers = headers[:len(headers)-1]
    head_length = len(headers.split(','))
    fout.write(headers + '\n')

    for cell in bs.find_all('td'):
        if commas == head_length: break
        stats += (cell.text.strip('\n') + ',').replace(' ', '')
        commas += 1
    stats = stats[:len(stats)-1].replace('\n', '')
    fout.write(stats)
    fout.close()


def uncomment_html(infile, outfile):
    f = open(infile, 'r')
    fout = open(outfile, 'w')
    line = f.readline()
    all = f.read()
    all_new = all.replace("<!--", "")
    all_new = all_new.replace("-->", "")
    fout.write(all_new)
    f.close()
    fout.close()

main()
