import pathlib
import requests
import os
import re
namelink=[]
tickers=[]
with open("tickers.txt") as fil:
    for line in fil:
        n=line.split("--->")
        namelink.append(n[1].rstrip())
        tickers.append(n[0].rstrip())
print(namelink,"-----------------")
path = '/Users/vishnuk/PycharmProjects/untitled1'
for j in range(len(namelink)):
    path1=path+'/'+namelink[j]
    #print(path1)
    str = tickers[j]
    pathlib.Path(path1).mkdir(parents=True, exist_ok=True)
    if tickers[j].__contains__('^'):
        str = tickers[j].replace('^', '%5E')
    if tickers[j].__contains__('='):
        str = tickers[j].replace('=', '%3D')
    print(str)
    f1 = open(path1+'/summary.html','w')
    append = 'https://finance.yahoo.com/quote/'+str+'?p='+str
    f1.write(requests.get(append).text)
    print(append)



    f2 = open(path1 + '/statistics.html', 'w')
    append = 'https://finance.yahoo.com/quote/'+str +'/key-statistics?p='+str
    f2.write(requests.get(append).text)
    print(append)


    f3 = open(path1 + '/financials.html', 'w')
    append = 'https://finance.yahoo.com/quote/'+str+'/financials?p='+str
    f3.write(requests.get(append).text)
    print(append)


    f4 = open(path1 + '/profile.html', 'w')
    append = 'https://finance.yahoo.com/quote/'+str+'/profile?p='+str
    f4.write(requests.get(append).text)
    print(append)


